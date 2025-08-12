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
public class Client {
    public static void main(String[] args) {
             try {
                 // Get the registry
                 Registry registry = LocateRegistry.getRegistry("localhost", 1099);

                 // Lookup the remote object
                 Hello stub = (Hello) registry.lookup("Hello");

                 // Call the remote method
                 String response = stub.sayHello();
                 System.out.println("Response: " + response);
             } catch (Exception e) {
                 System.err.println("Client exception: " + e.toString());
                 e.printStackTrace();
             }
         }

}
