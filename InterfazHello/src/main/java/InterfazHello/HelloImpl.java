package InterfazHello;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author FERCHO
 */
public class HelloImpl extends UnicastRemoteObject implements Hello{
    
    protected HelloImpl()throws RemoteException{
        super();
    }
    
    public String sayHello() throws RemoteException{
        return"Hello World";
    } 
    //implementación
    public MyObject proccessData(String data, int value) throws RemoteException{
        return new MyObject(data, value);
    }
    
}
