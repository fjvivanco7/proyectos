/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Conexion;

import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

/**
 *
 * @author FERCHO
 */
public class CConexion {
    private static CConexion instancia = new CConexion();
    
    private EntityManagerFactory entidadConexion;
    
    private CConexion(){
        
        entidadConexion = Persistence.createEntityManagerFactory("conexionCrud");
    }

    public static CConexion getInstancia() {
        return instancia;
    }

    public EntityManagerFactory getEntidadConexion() {
        return entidadConexion;
    }
    
    
    
}
