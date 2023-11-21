import sys

from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node

import tkinter as tk


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def maind():
    rclpy.init()

    minimal_client = MinimalClientAsync()
    response = minimal_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    minimal_client.get_logger().info(
        'Result of add_two_ints: for %d + %d = %d' %
        (int(sys.argv[1]), int(sys.argv[2]), response.sum))

    minimal_client.destroy_node()
    rclpy.shutdown()

def main():
    rclpy.init()
    minimal_client = MinimalClientAsync()
    

    # Création de la fenêtre
    fenetre = tk.Tk()
    fenetre.title("Fenêtre tkinter")

    # Création des étiquettes et des champs d'entrée
    label_nombre1 = tk.Label(fenetre, text="Nombre 1:")
    label_nombre1.pack()

    entry_nombre1 = tk.Entry(fenetre)
    entry_nombre1.pack()

    label_nombre2 = tk.Label(fenetre, text="Nombre 2:")
    label_nombre2.pack()

    entry_nombre2 = tk.Entry(fenetre)
    entry_nombre2.pack()

    # Fonction pour afficher les valeurs entrées lors du clic sur le bouton
    def afficher_valeurs():
        valeur1 = entry_nombre1.get()
        valeur2 = entry_nombre2.get()
        reponse = minimal_client.send_request(int(valeur1),int(valeur2))
        minimal_client.get_logger().info(
        'Result of add_two_ints: for %d + %d = %d' %
        (int(valeur1), int(valeur2), reponse.sum))

    # Création d'un bouton pour déclencher l'affichage des valeurs
    bouton_afficher = tk.Button(fenetre, text="Afficher valeurs", command=afficher_valeurs)
    bouton_afficher.pack()

    # Boucle principale
    fenetre.mainloop()
    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()