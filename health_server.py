#!/usr/bin/env python3
"""
Simple health check server for Railway
Runs alongside the main worker to provide health monitoring
"""

import json
import os
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from src.utils import setup_logging
from loguru import logger


class HealthHandler(BaseHTTPRequestHandler):
    """HTTP handler for health checks"""
    
    def do_GET(self):
        """Handle GET requests"""
        
        if self.path == '/health':
            self.send_health_check()
        elif self.path == '/status':
            self.send_system_status()
        else:
            self.send_404()
    
    def send_health_check(self):
        """Send basic health check response"""
        try:
            response = {
                "status": "healthy",
                "timestamp": datetime.now().isoformat(),
                "service": "jachtexamen-blog-worker",
                "environment": os.getenv("ENVIRONMENT", "unknown")
            }
            
            self.send_json_response(200, response)
            
        except Exception as e:
            logger.error(f"Health check error: {e}")
            self.send_json_response(500, {"status": "error", "message": str(e)})
    
    def send_system_status(self):
        """Send detailed system status"""
        try:
            # Check last run status
            last_run_file = "/tmp/last_blog_run.txt"
            last_run = None
            
            if os.path.exists(last_run_file):
                with open(last_run_file, 'r') as f:
                    last_run = f.read().strip()
            
            response = {
                "status": "operational",
                "timestamp": datetime.now().isoformat(),
                "service": "jachtexamen-blog-worker",
                "last_run": last_run,
                "environment": os.getenv("ENVIRONMENT", "development"),
                "run_mode": os.getenv("RAILWAY_RUN_MODE", "once"),
                "posting_frequency": {
                    "min_days": os.getenv("MIN_DAYS_BETWEEN_POSTS", "1"),
                    "max_days": os.getenv("MAX_DAYS_BETWEEN_POSTS", "3")
                }
            }
            
            self.send_json_response(200, response)
            
        except Exception as e:
            logger.error(f"Status check error: {e}")
            self.send_json_response(500, {"status": "error", "message": str(e)})
    
    def send_json_response(self, status_code, data):
        """Send JSON response"""
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response_json = json.dumps(data, indent=2)
        self.wfile.write(response_json.encode())
    
    def send_404(self):
        """Send 404 response"""
        self.send_response(404)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Not Found')
    
    def log_message(self, format, *args):
        """Override default logging to use loguru"""
        logger.info(f"HTTP: {format % args}")


def start_health_server(port=8000):
    """Start the health check server"""
    setup_logging("INFO")
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, HealthHandler)
    
    logger.info(f"🏥 Health server starting on port {port}")
    logger.info(f"📍 Health check: http://localhost:{port}/health")
    logger.info(f"📊 Status check: http://localhost:{port}/status")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("🛑 Health server stopped")
        httpd.shutdown()


if __name__ == "__main__":
    port = int(os.getenv('PORT', 8000))
    start_health_server(port) 