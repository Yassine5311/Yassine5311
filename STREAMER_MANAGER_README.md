# Streamer Manager

A simple Python script to manage and watch your favorite streamers with MPV.

## Features

- 📺 **Watch**: Browse and play your saved streamers in MPV
- ➕ **Add Streamer**: Add new streamers with name and URL
- 💾 **Persistent Storage**: Streamers are saved in a JSON file
- 🎯 **Simple Interface**: Easy-to-use command-line menu

## Prerequisites

- Python 3.x
- MPV media player (for watching streams)

### Installing MPV

#### Ubuntu/Debian
```bash
sudo apt install mpv
```

#### macOS
```bash
brew install mpv
```

#### Windows
Download from: https://mpv.io/installation/

## Usage

### Running the Script

```bash
python3 streamer_manager.py
```

Or make it executable and run directly:
```bash
chmod +x streamer_manager.py
./streamer_manager.py
```

### Main Menu Options

1. **Watch** - Display all saved streamers and select one to watch
2. **Add Streamer** - Add a new streamer with name and URL
3. **Exit** - Exit the program

### Adding a Streamer

1. Select option `2` from the main menu
2. Enter the streamer's name (e.g., "xQc", "Shroud")
3. Enter the streamer's URL (e.g., "https://twitch.tv/xqc")
4. The streamer will be saved automatically

### Watching a Stream

1. Select option `1` from the main menu
2. Choose a streamer from the numbered list
3. MPV will launch and start playing the stream

## Data Storage

Streamers are stored in `streamers.json` in the same directory as the script. The file is automatically created when you add your first streamer.

Example `streamers.json`:
```json
{
  "xQc": "https://twitch.tv/xqc",
  "Shroud": "https://twitch.tv/shroud",
  "Ninja": "https://youtube.com/@Ninja/live"
}
```

## Examples

### Adding Multiple Streamers
```
Enter your choice (1-3): 2
=== Add Streamer ===
Enter streamer name: xQc
Enter streamer URL: https://twitch.tv/xqc
✓ Streamer 'xQc' added successfully!
```

### Watching a Stream
```
Enter your choice (1-3): 1
=== Available Streamers ===
1. xQc
2. Shroud
3. Ninja

Select a streamer (number) or 'q' to quit: 1
Launching xQc in MPV...
URL: https://twitch.tv/xqc
```

## Error Handling

- Empty names or URLs are not allowed
- Invalid menu selections show helpful error messages
- Missing MPV installation shows installation instructions
- Corrupted JSON files are handled gracefully

## License

This is a simple utility script - feel free to use and modify as needed!
