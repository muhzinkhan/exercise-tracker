# Exercise Tracker

## Overview

The Exercise Tracker is a powerful Python application that leverages Nutritionix APIs for exercise data retrieval and the Sheety API to store this data in the user's Google Sheet. This enables users to effortlessly monitor their exercise progress by simply typing in natural language prompts.

## Features

- Utilizes Nutritionix APIs for comprehensive exercise data.
- Employs Natural Language Processing for user-friendly interaction.
- Stores exercise data in the user's Google Sheet via the Sheety API.
- Offers easy access to progress records anytime, anywhere.

## Documentation

For detailed information on the Nutritionix APIs used in this project, refer to the [Nutritionix API Documentation](https://developer.nutritionix.com/docs).

## Requirements

- Python 3.x
- Nutritionix API Key
- Sheety API Key

## Installation

1. Clone or download the repository to your local machine.
2. Ensure you have Python 3.x installed on your system.
3. Sign up for a Nutritionix API Key and a Sheety API Key.
4. Create a `config.py` file with your API keys. Use the `config_template.py` as a template.

## Usage

1. Open the `config.py` file and replace the placeholder values with your Nutritionix and Sheety API keys.
2. Run the `exercise_tracker.py` file.
3. Follow the prompts to input your exercise details.

## Configuration

You can customize the following parameters in `config.py`:

- `NUTRITIONIX_APP_ID`: Your Nutritionix application ID.
- `NUTRITIONIX_API_KEY`: Your Nutritionix API key.
- `SHEETY_ENDPOINT`: Sheety API endpoint for Google Sheets integration.
- `SHEETY_TOKEN`: Your Sheety API token.

## Acknowledgments

- [Nutritionix](https://developer.nutritionix.com/docs) for their comprehensive exercise data API.
- [Sheety](https://sheety.co/) for enabling seamless Google Sheets integration.

## Contributing

If you'd like to contribute, please fork the repository and create a pull request. Please make sure to update tests as appropriate.

## Support

If you encounter any issues or have suggestions, please [open an issue](https://github.com/yourusername/exercise-tracker/issues).

## Roadmap

- [ ] Implement user authentication for enhanced security.
- [ ] Add visualization features for exercise progress tracking.
- [ ] Provide multi-language support for Natural Language Processing.

## Authors

- [Muhsin Khan](https://github.com/muhzinkhan)

## Disclaimer

This application is provided as-is, without any warranty or guarantee of any kind. Use at your own risk.
