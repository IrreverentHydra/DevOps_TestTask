import itertools
import json

def generate_versions(template):
    """Генерирует версии на основе шаблона"""
    parts = template.split(".")
    versions = []
    for part in parts:
        if part == '*':
            versions.append(['1', '9'])
        else:
            versions.append([part])
    return [".".join(version) for version in itertools.product(*versions)]

def load_configurations(filename):
    """Загружает конфигурацию"""
    with open(filename, 'r') as file:
        return json.load(file)
    
def generate_all_versions(config):
    """Генерирует версии на основе шаблонов"""
    all_versions = []
    for template in config.values():
        all_versions.extend(generate_versions(template))
    return sorted(all_versions, key = lambda v: list(map(int, v.split('.'))))

def filter_versions(versions, base_version):
    """Фильтрует версии, которые меньше указанной"""
    base_parts = list(map(int, base_version.split('.')))
    filtered_versions = [
        v for v in versions if list(map(int, v.split('.'))) < base_parts
    ]
    return filter_versions

def generate_and_filter_versions(product_version, config_file):
    """Генерирует версии и фильтрует их"""
    config = load_configurations(config_file)
    all_versions = generate_all_versions(config)
    print("All generated versions:", all_versions)

    older_versions = filter_versions(all_versions, product_version)
    print("Versions older than", product_version, ":", filter_versions)
