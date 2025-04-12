"""
MCP (Model-Context-Protocol) 伺服器

這個伺服器提供了一個網路接口來控制電子郵件發送程序。它支援以下功能：

1. 網路通信：
   - 使用 TCP/IP 協議
   - 支援多個客戶端連接
   - 每個客戶端獨立處理
   - 支援 netcat 連接

2. 電子郵件控制：
   - 啟動電子郵件發送程序
   - 停止電子郵件發送程序
   - 狀態監控

3. 日誌記錄：
   - 所有操作都會被記錄到日誌檔案
   - 日誌檔案位置：logger/email.log
   - 自動創建日誌目錄

使用方法：
1. 啟動伺服器：
   python3 mcp_server.py

2. 連接到伺服器（使用 netcat）：
   nc localhost 12345

3. 發送命令：
   - start_email_publisher：啟動電子郵件發送程序
   - stop_email_publisher：停止電子郵件發送程序

注意：
- 在 macOS 上，我們使用 netcat (nc) 來替代 telnet
- 按 Ctrl+C 來停止伺服器
- 所有操作都會被記錄在 logger/email.log 中
"""
import socket
import threading
import subprocess
import logging
import json
from pathlib import Path

def load_config():
    """載入配置文件"""
    # 使用相對路徑從sample目錄加載配置文件
    current_dir = Path(__file__).parent
    config_path = current_dir / "sample" / "mcp_config.json"
    
    if not config_path.exists():
        raise FileNotFoundError(f"找不到配置文件: {config_path}")
    
    with open(config_path, 'r') as f:
        return json.load(f)

# 載入配置
config = load_config()

# 確保日誌目錄存在
log_dir = Path(__file__).parent / config["mcpServers"]["email_pub"]["log_dir"]
if not log_dir.exists():
    log_dir.mkdir()

# 設置日誌
logging.basicConfig(
    level=config["mcpServers"]["email_pub"]["log_level"],
    format=config["mcpServers"]["email_pub"]["log_format"],
    filename=str(log_dir / config["mcpServers"]["email_pub"]["log_file"]),
    filemode='a'
)
logger = logging.getLogger(__name__)

class MCP_Server:
    def __init__(self):
        self.config = config
        self.host = config["mcpServers"]["email_pub"]["host"]
        self.port = config["mcpServers"]["email_pub"]["port"]
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clients = []
        self.threads = []
        self.process = None

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        logger.info(f"MCP伺服器啟動於 {self.host}:{self.port}")
        
        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                logger.info(f"新連接: {client_address}")
                self.clients.append(client_socket)
                thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                self.threads.append(thread)
                thread.start()
        except KeyboardInterrupt:
            self.shutdown()

    def handle_client(self, client_socket):
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                
                command = data.decode('utf-8').strip()
                logger.info(f"收到命令: {command}")
                
                if command == "start_email_publisher":
                    self.start_email_publisher()
                elif command == "stop_email_publisher":
                    self.stop_email_publisher()
                else:
                    response = f"未知命令: {command}\n可用命令: start_email_publisher, stop_email_publisher\n"
                    client_socket.sendall(response.encode('utf-8'))
                    
        except Exception as e:
            logger.error(f"處理客戶端時發生錯誤: {str(e)}")
        finally:
            client_socket.close()
            self.clients.remove(client_socket)

    def start_email_publisher(self):
        """啟動 emailPublisher.py 程式"""
        try:
            if self.process and self.process.poll() is None:
                logger.warning("電子郵件發送程序已在運行")
                return
            
            # Get paths from config
            script_path = config["mcpServers"]["email_pub"]["script_path"]
            python_path = config["mcpServers"]["email_pub"]["python_path"]
            
            if not Path(script_path).exists():
                logger.error(f"找不到程式: {script_path}")
                return
            
            try:
                self.process = subprocess.Popen(
                    [python_path, script_path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    stdin=subprocess.PIPE
                )
                logger.info("電子郵件發送程序已啟動")
                
                # Optionally, you can read the output
                # stdout, stderr = self.process.communicate(timeout=5)
                
            except subprocess.TimeoutExpired:
                logger.error("啟動電子郵件發送程序超時")
            except Exception as e:
                logger.error(f"啟動電子郵件發送程序時發生錯誤: {str(e)}")
                
        except Exception as e:
            logger.error(f"處理電子郵件發送程序時發生錯誤: {str(e)}")

    def stop_email_publisher(self):
        """停止 emailPublisher.py 程式"""
        try:
            if self.process and self.process.poll() is None:
                self.process.terminate()
                self.process.wait(timeout=5)
                logger.info("電子郵件發送程序已停止")
            else:
                logger.warning("沒有正在運行的電子郵件發送程序")
        except Exception as e:
            logger.error(f"停止電子郵件發送程序時發生錯誤: {str(e)}")

    def shutdown(self):
        logger.info("關閉伺服器...")
        self.stop_email_publisher()
        
        for client in self.clients:
            client.close()
        self.server_socket.close()
        
        for thread in self.threads:
            thread.join()

if __name__ == "__main__":
    server = MCP_Server()
    server.start()