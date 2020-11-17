import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description='Quoridor - Phase 1')
    parser.add_argument('IDUL', help='IDUL du joueur')
    parser.add_argument('-p', '--parties', dest='parties', action='store_true', help='Lister les identifiants de vos 20 dernières parties')
    return parser.parse_args()
