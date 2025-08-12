/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package InterfazHello;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

/**
 *
 * @author FERCHO
 */
public class Server {
    public static void main(String[] args) {
             try {
                 // Create an instance of the implementation class
                 HelloImpl obj = new HelloImpl();

                 // Bind the remote object's stub in the registry
                 Registry registry = LocateRegistry.createRegistry(1099);
                 registry.bind("Hello", obj);

                 System.out.println("Server ready");
             } catch (Exception e) {
                 System.err.println("Server exception: " + e.toString());
                 e.printStackTrace();
             }
         }

}
