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

- [Python 3.x]()
- [Nutritionix API](https://developer.nutritionix.com/docs) Key
- [Sheety API](https://sheety.co/) Key
- [Google spreadsheet](https://docs.google.com/spreadsheets/create)

## Installation

1. Clone or download the repository to your local machine.
2. Ensure you have Python 3.x installed on your system.
3. Sign up for a [Nutritionix API](https://developer.nutritionix.com/docs) Key and a [Sheety API](https://sheety.co/) Key.
4. Create a `.env` file your with your API keys to store your environment variables.
Refer [python-dotenv](https://pypi.org/project/python-dotenv/) to setup env variables.

## Usage

1. Open the setup `.env` file.
2. Run the `exercise_tracker.py` file.
3. Follow the prompts to input your exercise details. You can type in as you would type to a chat bot.
Example: *I ran 5 km for 30 min*
4. The script will respond, calculating your calories and other data as well and populate the spreadsheet.

## Configuration

Configure env variables in `.env`:

- `NUTRITIONIX_APP_ID`: Your Nutritionix application ID.
- `NUTRITIONIX_API_KEY`: Your Nutritionix API key.
- `SHEETY_AUTH_TOKEN`: Your Sheety API token.
- `SHEETY_ENDPOINT`: Sheety API endpoint for Google Sheets integration.
- `G_SPREADSHEET_LINK`: Your Google sheet's link.
- `GENDER`: Your Stats.
- `WEIGHT_KG`: Your Stats.
- `HEIGHT_CM`: Your Stats.
- `AGE`: Your Stats.

## Acknowledgments

- [Nutritionix](https://developer.nutritionix.com/docs) for their comprehensive exercise data API.
- [Sheety](https://sheety.co/) for enabling seamless Google Sheets integration.

## Contributing

If you'd like to contribute, please fork the repository and create a pull request. Please make sure to update tests as appropriate.

## Support

If you encounter any issues or have suggestions, please [open an issue](https://github.com/yourusername/exercise-tracker/issues).

## Roadmap

- [ ] Implement user authentication for enhanced security.
- [ ] Add visualization features for exercise progress tracking using [pixela](https://pixe.la/).

## Authors

- [Muhsin Khan](https://github.com/muhzinkhan)

## Disclaimer

This application is provided as-is, without any warranty or guarantee of any kind. Use at your own risk.
