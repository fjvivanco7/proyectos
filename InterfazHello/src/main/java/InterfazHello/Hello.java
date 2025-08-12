/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package InterfazHello;

/**
 *
 * @author FERCHO
 */
import java.rmi.Remote;
import java.rmi.RemoteException;

     public interface Hello extends Remote {
         String sayHello()throws RemoteException;
         MyObject processData(String data, int value) throws RemoteException;
     }
