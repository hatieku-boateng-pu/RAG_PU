# Voice Chat Feature Guide

## Overview

The Streamlit AI Knowledge Assistant includes a **live voice chat** feature that allows users to interact with the assistant using voice input and receive audio responses.

## Features

### 🎙️ Voice Input
- **Record Questions**: Use your microphone to ask questions instead of typing
- **Real-time Transcription**: Audio is transcribed using OpenAI's Whisper model
- **Duplicate Detection**: Smart hash-based detection prevents reprocessing the same recording
- **Visual Feedback**: See the transcription before it's processed

### 🔊 Audio Output
- **Text-to-Speech**: Assistant responses are automatically converted to audio
- **Natural Voice**: Uses OpenAI's TTS with the "alloy" voice by default
- **Auto-playback**: Audio plays automatically in the chat interface
- **Format**: MP3 audio for broad compatibility

## How to Use

### 1. Enable Voice Chat

1. Open the Streamlit app
2. Look for the **🎙️ Voice Chat** section in the sidebar
3. Toggle **"Enable voice input and audio replies"** to ON

### 2. Ask Questions with Your Voice

1. Expand the **"🎙️ Ask with your voice"** section in the main chat area
2. Click the microphone icon to start recording
3. Speak your question clearly
4. Click stop when done
5. Wait for transcription to appear
6. The assistant will process your question and respond

### 3. Listen to Responses

- When voice chat is enabled, assistant responses automatically generate audio
- Audio players appear below each assistant message
- Click play to hear the response
- Audio controls allow pause/resume and volume adjustment

## Requirements

### Technical Requirements
- **Streamlit**: Version 1.32.0 or higher (for `audio_input` support)
- **Browser**: Modern browser with microphone access and HTML5 audio support
- **API Key**: Valid OpenAI API key with access to:
  - Whisper transcription model
  - TTS (Text-to-Speech) model
  - Chat completion models

### Environment Configuration

The following environment variables can be set in your `.env` file:

```env
# Required
OPENAI_API_KEY=your_api_key_here

# Optional - Voice Chat Configuration
OPENAI_TRANSCRIBE_MODEL=gpt-4o-mini-transcribe  # Default transcription model
OPENAI_TTS_MODEL=gpt-4o-mini-tts                # Default TTS model
OPENAI_TTS_VOICE=alloy                          # Voice selection
```

### Available TTS Voices

Choose from the following OpenAI TTS voices:
- `alloy` (default) - Neutral, balanced voice
- `echo` - Warm, upbeat voice
- `fable` - Expressive, dramatic voice
- `onyx` - Deep, authoritative voice
- `nova` - Energetic, friendly voice
- `shimmer` - Soft, calm voice

## Limitations

### Current Limitations

1. **Response Length**: Responses longer than 2000 characters will not generate audio
   - You'll see a warning if this occurs
   - The text response is still displayed

2. **Processing Time**: 
   - Transcription takes 2-5 seconds depending on audio length
   - TTS generation takes 1-3 seconds per response
   - Processing is synchronous (blocks UI temporarily)

3. **Audio Format**:
   - Input: Requires WAV format from browser recording
   - Output: Fixed to MP3 format

4. **No Audio Caching**: Each response regenerates audio (no caching for repeated queries)

5. **Formatting in Audio**: Text formatting (bold, links, etc.) may sound awkward when read aloud

## Troubleshooting

### Voice Chat Toggle is Disabled

**Problem**: The toggle appears grayed out with message "Upgrade Streamlit to use voice input."

**Solution**: 
```bash
pip install --upgrade streamlit
```
Ensure Streamlit version is 1.32.0 or higher.

### Microphone Not Working

**Problem**: Browser doesn't detect microphone or recording fails.

**Solutions**:
1. Check browser permissions - allow microphone access for the app
2. Verify microphone is connected and working in system settings
3. Try a different browser (Chrome and Firefox have best support)
4. Check if other apps can access the microphone

### Transcription Errors

**Problem**: "Error transcribing audio" message appears.

**Possible Causes**:
1. **API Key Issues**: Invalid or expired OpenAI API key
2. **Audio Format**: Recording may be corrupted or invalid format
3. **Network Issues**: Connection problems to OpenAI API
4. **Quota Limits**: API usage limits reached

**Solutions**:
1. Verify your OpenAI API key is valid
2. Check your OpenAI account has available credits
3. Try recording again with clear audio
4. Check console logs for detailed error messages

### No Audio Playback

**Problem**: Responses don't generate audio even with voice chat enabled.

**Possible Causes**:
1. Response is longer than 2000 characters
2. TTS generation failed
3. Browser audio playback issues

**Solutions**:
1. Try asking shorter questions for shorter responses
2. Check browser console for TTS errors
3. Verify browser audio isn't muted
4. Try refreshing the page

### Audio Quality Issues

**Problem**: Audio is unclear or has artifacts.

**Solutions**:
1. Record in a quiet environment with minimal background noise
2. Speak clearly and at a moderate pace
3. Position microphone appropriately
4. Try a different voice by setting `OPENAI_TTS_VOICE` in `.env`

## Best Practices

### For Voice Input
- Speak clearly and at a natural pace
- Minimize background noise
- Keep questions concise (30-60 seconds max)
- Wait for transcription before recording again

### For Audio Output
- Use headphones in public spaces
- Adjust volume appropriately
- For long responses, consider disabling voice chat and reading text
- Review transcription for accuracy before submission

## Privacy & Security

### Data Handling
- **Audio Processing**: Audio is sent to OpenAI for transcription
- **Text Processing**: Responses are sent to OpenAI for TTS generation
- **Temporary Storage**: Audio data is not permanently stored by the app
- **OpenAI Policies**: Subject to OpenAI's data usage and privacy policies

### Recommendations
- Don't record sensitive or confidential information
- Be aware audio is processed by third-party services (OpenAI)
- Review OpenAI's privacy policy and terms of service
- Use text input for sensitive queries

## Implementation Details

### Code Structure

The voice chat feature is implemented in `streamlit_app.py`:

1. **Session State** (lines 354-358):
   ```python
   if "last_audio_hash" not in st.session_state:
       st.session_state.last_audio_hash = None
   if "voice_chat_enabled" not in st.session_state:
       st.session_state.voice_chat_enabled = False
   ```

2. **Transcription Function** (lines 469-484):
   ```python
   def _transcribe_audio(audio_bytes: bytes) -> str | None:
       # Converts audio bytes to text using OpenAI Whisper
   ```

3. **TTS Function** (lines 487-508):
   ```python
   def _synthesize_speech(text: str) -> bytes | None:
       # Converts text to audio using OpenAI TTS
   ```

4. **UI Toggle** (lines 872-882):
   ```python
   st.session_state.voice_chat_enabled = st.toggle(
       "Enable voice input and audio replies",
       value=st.session_state.voice_chat_enabled,
       disabled=not voice_supported,
   )
   ```

5. **Voice Input UI** (lines 961-978):
   ```python
   if st.session_state.get("voice_chat_enabled"):
       with st.expander("🎙️ Ask with your voice"):
           audio_prompt = st.audio_input("Record a question")
           # Process audio and transcribe
   ```

6. **Audio Playback** (lines 751-754):
   ```python
   if st.session_state.get("voice_chat_enabled"):
       audio_bytes = _synthesize_speech(response)
       if audio_bytes:
           st.audio(audio_bytes, format="audio/mp3")
   ```

## Cost Considerations

Voice chat uses OpenAI's paid APIs:

### Pricing (as of implementation)
- **Whisper (Transcription)**: ~$0.006 per minute of audio
- **TTS (Text-to-Speech)**: ~$0.015 per 1000 characters

### Example Costs
- 1-minute voice question: ~$0.006
- 500-character response (TTS): ~$0.0075
- **Total per voice interaction**: ~$0.01-0.02

### Cost Optimization Tips
1. Use voice chat selectively for important queries
2. Keep questions concise to reduce transcription costs
3. Disable TTS for long responses (over 2000 chars is blocked)
4. Consider text input for quick follow-up questions
5. Monitor OpenAI API usage in your dashboard

## Future Enhancements

Potential improvements for future versions:

- [ ] Streaming TTS for faster response times
- [ ] Audio caching to avoid regenerating same responses
- [ ] Voice speed/pitch controls in UI
- [ ] Interrupt/stop button for audio playback
- [ ] Support for multiple languages
- [ ] Preprocessing text to remove markdown before TTS
- [ ] Background noise reduction
- [ ] Audio quality selection (standard/HD)
- [ ] Conversation export with audio files
- [ ] Voice activity detection for hands-free mode

## Support

For issues or questions:
1. Check this guide's troubleshooting section
2. Review the main README.md for general setup
3. Consult OpenAI API documentation for API-specific issues
4. Check Streamlit documentation for UI component issues

---

**Last Updated**: February 2026  
**Streamlit Version**: 1.53.0  
**OpenAI SDK Version**: Latest
