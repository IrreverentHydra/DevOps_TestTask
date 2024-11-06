import sys
from src.fetch_time import calculate_average_delta
from src.generate_versions import generate_and_filter_versions

def main():
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [args]")
        print("Commands:")
        print("  fetch_time                - Запуск скрипта для работы с API времени")
        print("  generate_versions <version> <config_file> - Генерация версий на основе шаблонов")
        sys.exit(1)
    
    command = sys.argv[1]

    if command == "fetch_time":
        calculate_average_delta()
    elif command == "generate_versions":
        if len(sys.argv) < 4:
            print("Usage: main.py generate_versions <product_version> <config_file>")
            sys.exit(1)
        product_version = sys.argv[2]
        config_file = sys.argv[3]
        generate_and_filter_versions(product_version, config_file)
    else:
        print("Unknown command:", command)

if __name__ == "__main__":
    main()
 