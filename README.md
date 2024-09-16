# GIF Grid Processor
#Video 1- https://www.loom.com/share/90e1139304c24dd48871b63ce1ebbafe?sid=a06ae1a5-aaab-4787-86f3-8ed2882b8493

#Video 2 - https://www.loom.com/share/90e1139304c24dd48871b63ce1ebbafe?sid=a06ae1a5-aaab-4787-86f3-8ed2882b8493

## Overview

The GIF Grid Processor is a web application that allows users to upload an animated GIF, split it into a grid of smaller animated GIFs, and display them in a synchronized manner on an HTML page. This application processes GIFs without relying on external libraries and can handle various grid sizes and dimensions.

## Features

- **GIF Processing**: Split an input animated GIF into an N x M grid of smaller animated GIFs.
- **Web Interface**: Upload GIFs, specify grid dimensions, and preview the result.
- **Synchronization**: All small GIFs play in unison to recreate the original animation.
- **Color Preservation**: Maintains the original colors of the GIF throughout the process.
- **User Input**: Allows users to upload their own GIFs and specify grid dimensions.
- **Error Handling**: Handles common issues like unsupported dimensions and empty grids.

## Requirements

1. **GIF Processing**:
   - Implemented in JavaScript (no external libraries).
   - GIFs are split and displayed as smaller GIFs in a grid.

2. **Web Interface**:
   - HTML page for uploading GIFs and specifying grid dimensions.
   - Display processed GIFs in a grid layout.

3. **Synchronization**:
   - Ensures all smaller GIFs are frame-synchronized.

4. **Color Preservation**:
   - Maintains original GIF colors.

5. **User Input**:
   - Allows file upload and grid dimension input.
   - Only even-sized grid inputs are allowed to avoid GIF breaks.

6. **Performance**:
   - Optimized for handling various GIF sizes efficiently.

## Installation and Setup

1. **Clone or Download the Repository**:
   - Clone the repository or download the source code.

2. **Navigate to the Project Directory**:
   - Open your terminal and navigate to the project directory.

3. **Set Up a Local Server (Optional)**:
   - Use a simple HTTP server for testing. Python provides a built-in HTTP server:
     ```bash
     python -m http.server
     ```
   - Open `http://localhost:8000` in your browser to view the application.

## Usage

1. **Open the Application**:
   - Launch the application in a web browser.

2. **Upload a GIF**:
   - Click on the "Choose File" button to select an animated GIF.

3. **Specify Grid Dimensions**:
   - Enter the number of rows and columns for the grid. Ensure dimensions are even numbers.

4. **Process the GIF**:
   - Click the "Process GIF" button to split the GIF into smaller GIFs and display them.

5. **Preview and View Results**:
   - View the uploaded GIF preview and processed GIFs in a grid layout.

## Troubleshooting

- **Broken Image/Error Messages**:
  - Ensure the GIF is correctly uploaded and not corrupted.
  - Verify that the grid dimensions are even numbers.

- **GIF Does Not Display Properly**:
  - Check the dimensions of the grid; ensure they are divisible by 2.
  - Make sure the GIF file is valid and properly encoded.

## Notes

- **File Handling**: The application does not currently clean up processed files after each operation. You might need to manually clear processed files if you use server-side handling.

- **Browser Compatibility**: Ensure your browser supports GIFs and has JavaScript enabled.

## Contributing

Feel free to submit issues or pull requests if you have improvements or bug fixes. For major changes, please discuss them with the maintainers before implementing.
