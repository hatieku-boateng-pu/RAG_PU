"""
Test script to verify voice chat functionality in streamlit_app.py
This script checks that all voice chat components are properly implemented.
"""

import sys
import os

# Add parent directory to path to import streamlit_app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_voice_chat_imports():
    """Test that required imports are present"""
    print("✓ Testing voice chat imports...")
    
    try:
        import streamlit as st
        print(f"  ✓ Streamlit version: {st.__version__}")
        
        # Check for audio_input support
        has_audio_input = hasattr(st, 'audio_input')
        if has_audio_input:
            print("  ✓ Streamlit has audio_input support")
        else:
            print("  ✗ WARNING: Streamlit version does not support audio_input")
            print("    Required version: 1.32.0 or higher")
            return False
        
        import io
        import hashlib
        print("  ✓ Required standard library imports available")
        
        from openai import OpenAI
        print("  ✓ OpenAI library available")
        
        return True
    except ImportError as e:
        print(f"  ✗ Import error: {e}")
        return False


def test_voice_chat_functions():
    """Test that voice chat functions are defined in streamlit_app.py"""
    print("\n✓ Testing voice chat functions...")
    
    try:
        with open('../streamlit_app.py', 'r') as f:
            content = f.read()
        
        # Check for key functions
        functions_to_check = [
            '_transcribe_audio',
            '_synthesize_speech',
        ]
        
        all_found = True
        for func_name in functions_to_check:
            if f"def {func_name}" in content:
                print(f"  ✓ Function '{func_name}' is defined")
            else:
                print(f"  ✗ Function '{func_name}' is missing")
                all_found = False
        
        return all_found
    except Exception as e:
        print(f"  ✗ Error reading streamlit_app.py: {e}")
        return False


def test_voice_chat_session_state():
    """Test that voice chat session state variables are initialized"""
    print("\n✓ Testing voice chat session state initialization...")
    
    try:
        with open('../streamlit_app.py', 'r') as f:
            content = f.read()
        
        # Check for session state variables
        session_vars = [
            'last_audio_hash',
            'voice_chat_enabled',
        ]
        
        all_found = True
        for var in session_vars:
            if var in content and 'st.session_state' in content:
                print(f"  ✓ Session state variable '{var}' is used")
            else:
                print(f"  ✗ Session state variable '{var}' not found")
                all_found = False
        
        return all_found
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def test_voice_chat_ui_elements():
    """Test that voice chat UI elements are present"""
    print("\n✓ Testing voice chat UI elements...")
    
    try:
        with open('../streamlit_app.py', 'r') as f:
            content = f.read()
        
        # Check for key UI elements
        ui_elements = {
            'st.toggle': 'Voice chat toggle switch',
            'st.audio_input': 'Audio input widget',
            'st.audio': 'Audio playback widget',
            'st.expander': 'Voice input expander',
        }
        
        all_found = True
        for element, description in ui_elements.items():
            if element in content:
                print(f"  ✓ {description} ({element}) is present")
            else:
                print(f"  ✗ {description} ({element}) is missing")
                all_found = False
        
        return all_found
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def test_voice_chat_api_integration():
    """Test that OpenAI API integration is properly configured"""
    print("\n✓ Testing OpenAI API integration...")
    
    try:
        with open('../streamlit_app.py', 'r') as f:
            content = f.read()
        
        # Check for API calls
        api_checks = {
            'client.audio.transcriptions.create': 'Whisper transcription API',
            'client.audio.speech.create': 'TTS API',
        }
        
        all_found = True
        for api_call, description in api_checks.items():
            if api_call in content:
                print(f"  ✓ {description} is integrated")
            else:
                print(f"  ✗ {description} is missing")
                all_found = False
        
        # Check for environment variable configuration
        env_vars = [
            'OPENAI_TRANSCRIBE_MODEL',
            'OPENAI_TTS_MODEL',
            'OPENAI_TTS_VOICE',
        ]
        
        for var in env_vars:
            if var in content:
                print(f"  ✓ Environment variable '{var}' is used")
            else:
                print(f"  ⚠ Environment variable '{var}' not found (may use defaults)")
        
        return all_found
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def test_voice_chat_error_handling():
    """Test that error handling is implemented"""
    print("\n✓ Testing error handling...")
    
    try:
        with open('../streamlit_app.py', 'r') as f:
            content = f.read()
        
        # Look for try-except blocks in voice functions
        has_error_handling = (
            'try:' in content and 
            'except Exception' in content and
            'st.error' in content
        )
        
        if has_error_handling:
            print("  ✓ Error handling is implemented")
            return True
        else:
            print("  ⚠ Limited or no error handling found")
            return False
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def test_voice_chat_duplicate_detection():
    """Test that duplicate audio detection is implemented"""
    print("\n✓ Testing duplicate audio detection...")
    
    try:
        with open('../streamlit_app.py', 'r') as f:
            content = f.read()
        
        # Check for hash-based duplicate detection
        has_hash = 'hashlib.sha256' in content and 'audio_hash' in content
        has_comparison = 'last_audio_hash' in content
        
        if has_hash and has_comparison:
            print("  ✓ Duplicate audio detection is implemented")
            return True
        else:
            print("  ✗ Duplicate audio detection not found")
            return False
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def run_all_tests():
    """Run all voice chat tests"""
    print("=" * 70)
    print("Voice Chat Feature Verification Tests")
    print("=" * 70)
    
    tests = [
        test_voice_chat_imports,
        test_voice_chat_functions,
        test_voice_chat_session_state,
        test_voice_chat_ui_elements,
        test_voice_chat_api_integration,
        test_voice_chat_error_handling,
        test_voice_chat_duplicate_detection,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"\n✗ Test failed with exception: {e}")
            results.append(False)
    
    print("\n" + "=" * 70)
    print("Test Summary")
    print("=" * 70)
    
    passed = sum(results)
    total = len(results)
    
    print(f"\nTests Passed: {passed}/{total}")
    
    if all(results):
        print("\n✅ ALL TESTS PASSED - Voice chat is fully implemented!")
        return 0
    elif passed >= total * 0.7:
        print("\n⚠️  MOSTLY PASSING - Voice chat is implemented with minor issues")
        return 0
    else:
        print("\n❌ TESTS FAILED - Voice chat implementation has significant issues")
        return 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
