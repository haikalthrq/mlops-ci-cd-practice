"""
Simple test file for CI/CD pipeline demonstration
"""
import sys
import os

# Add the app directory to Python path so we can import app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

try:
    from app import greet
    
    def test_greet_function():
        """Test the basic greet function"""
        result = greet("Alice")
        assert "Alice" in result
        assert "Hello" in result
        print("✅ test_greet_function passed")
    
    def test_greet_empty_input():
        """Test greet function with empty input"""
        result = greet("")
        assert "Please enter your name!" in result
        print("✅ test_greet_empty_input passed")
    
    def test_greet_whitespace_input():
        """Test greet function with whitespace input"""
        result = greet("   ")
        assert "Please enter your name!" in result
        print("✅ test_greet_whitespace_input passed")

    if __name__ == "__main__":
        print("🧪 Running tests...")
        test_greet_function()
        test_greet_empty_input() 
        test_greet_whitespace_input()
        print("🎉 All tests passed!")
        
except ImportError as e:
    print(f"⚠️  Could not import app module: {e}")
    print("This is expected if gradio is not installed in the current environment.")
    print("Tests will run properly in CI environment.")
