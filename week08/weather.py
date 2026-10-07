import argparse
import os
import sys

from favorites import FavoritesManager
from weather_api import WeatherAPI, format_current_weather, format_forecast


FAVORITES_FILE = "week08/favorites.json"


def load_api_key():
    api_key = os.getenv("WEATHER_API_KEY")

    if api_key:
        return api_key

    try:
        import config
        return config.WEATHER_API_KEY
    except (ImportError, AttributeError):
        return None


def build_parser():
    parser = argparse.ArgumentParser(description="Weather CLI application")

    subparsers = parser.add_subparsers(dest="command", required=True)

    current_parser = subparsers.add_parser("current")
    current_parser.add_argument("location")

    forecast_parser = subparsers.add_parser("forecast")
    forecast_parser.add_argument("location")
    forecast_parser.add_argument("--days", type=int, default=3)

    favorites_parser = subparsers.add_parser("favorites")
    favorites_subparsers = favorites_parser.add_subparsers(
        dest="favorites_command",
        required=True,
    )

    add_parser = favorites_subparsers.add_parser("add")
    add_parser.add_argument("name")
    add_parser.add_argument("location")

    favorites_subparsers.add_parser("list")

    remove_parser = favorites_subparsers.add_parser("remove")
    remove_parser.add_argument("name")

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    favorites = FavoritesManager(FAVORITES_FILE)

    if args.command == "favorites":
        if args.favorites_command == "add":
            if not favorites.add(args.name, args.location):
                print(
                    f"Favorite '{args.name}' already exists.",
                    file=sys.stderr,
                )
                return 1

            print(f"Added favorite '{args.name}'.")
            return 0

        if args.favorites_command == "list":
            for name, location in favorites.list_all().items():
                print(f"{name}: {location}")
            return 0

        if args.favorites_command == "remove":
            if not favorites.remove(args.name):
                print(
                    f"Favorite '{args.name}' not found.",
                    file=sys.stderr,
                )
                return 1

            print(f"Removed favorite '{args.name}'.")
            return 0

    api_key = load_api_key()

    if not api_key:
        print("Weather API key is missing.", file=sys.stderr)
        return 1

    location = favorites.get_location(args.location) or args.location
    api = WeatherAPI(api_key)

    if args.command == "current":
        data = api.get_current_weather(location)

        if data is None:
            print("Failed to retrieve weather data.", file=sys.stderr)
            return 1

        print(format_current_weather(data))
        return 0

    if args.command == "forecast":
        try:
            data = api.get_forecast(location, args.days)
        except ValueError as error:
            print(error, file=sys.stderr)
            return 1

        if data is None:
            print("Failed to retrieve weather data.", file=sys.stderr)
            return 1

        print(format_forecast(data))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
