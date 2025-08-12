/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package InterfazHello;

import java.io.Serializable;

/**
 *
 * @author FERCHO
 */
class MyObject implements Serializable {
    private String message;
    private int number;
    
    public MyObject(String message, int number){
        this.message=message;
        this.number=number;
    }
    
    public String getMessage(){
        return message;
    }
    
    public int getNumber(){
        return number;
    }
    public String toString(){
        return"MyObject";
    }
    
}
