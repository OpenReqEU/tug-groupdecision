#!/usr/bin/env python3

import connexion
from application import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Requirement Detection Service'})
    app.run(port=9008)


if __name__ == '__main__':
    main()
