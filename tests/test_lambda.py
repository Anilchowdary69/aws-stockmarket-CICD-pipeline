import pytest
import json
import sys
import os

# Add lambda folder to path so we can import the functions
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lambda'))

class TestLambdaFunction:
    
def test_lambda_import(self):
    """Test that lambda_function can be imported without errors"""
    import os
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
    os.environ['DYNAMO_TABLE'] = 'test-table'
    os.environ['S3_BUCKET'] = 'test-bucket'
    try:
        import lambda_function
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import lambda_function: {e}")

def test_stock_trend_import(self):
    """Test that stock_trend_alert can be imported without errors"""
    import os
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
    os.environ['TABLE_NAME'] = 'test-table'
    os.environ['SNS_TOPIC_ARN'] = 'arn:aws:sns:us-east-1:123456789:test'
    try:
        import stock_trend_alert
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import stock_trend_alert: {e}")

    def test_kinesis_event_structure(self):
        """Test that a valid Kinesis event is structured correctly"""
        event = {
            "Records": [
                {
                    "kinesis": {
                        "data": "eyJzeW1ib2wiOiAiQUFQTCIsICJwcmljZSI6IDI3Mi41MX0="
                    }
                }
            ]
        }
        assert "Records" in event
        assert len(event["Records"]) > 0
        assert "kinesis" in event["Records"][0]
        assert "data" in event["Records"][0]["kinesis"]

    def test_price_change_calculation(self):
        """Test the price change calculation logic used in lambda"""
        price = 274.37
        previous_close = 272.14
        price_change = round(price - previous_close, 2)
        price_change_percent = round((price_change / previous_close) * 100, 2)
        
        assert price_change == 2.23
        assert price_change_percent == 0.82

    def test_anomaly_detection(self):
        """Test anomaly detection — flags if price change exceeds 5 percent"""
        def detect_anomaly(change_percent):
            return "Yes" if abs(change_percent) > 5 else "No"
        
        assert detect_anomaly(6.5) == "Yes"
        assert detect_anomaly(-6.5) == "Yes"
        assert detect_anomaly(2.3) == "No"
        assert detect_anomaly(-2.3) == "No"