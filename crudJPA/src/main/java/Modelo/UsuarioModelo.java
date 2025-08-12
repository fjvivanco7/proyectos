/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Modelo;

import Entidades.Usuarios;
import java.util.List;
import javax.persistence.EntityManager;
import javax.persistence.Query;

/**
 *
 * @author FERCHO
 */
public class UsuarioModelo {
    
    private EntityManager entityManager(){
        
        return Conexion.CConexion.getInstancia().getEntidadConexion().createEntityManager();
    
    }
    
    public List<Usuarios>mostrar(){
        
        Query q = entityManager().createQuery("SELECT u FROM Usuarios u");
        
        return q.getResultList();
    }
    
    public void crear(Usuarios usuarios){
        
        EntityManager entidad = entityManager();
        try{
        entidad.getTransaction().begin();
        entidad.persist(usuarios);
        entidad.getTransaction().commit();
        
        }catch(Exception e){
            
            entidad.getTransaction().rollback();
        }
        
    }
    
    public void editar(Usuarios usuarios){
        
        EntityManager entidad = entityManager();
        try{
        entidad.getTransaction().begin();
        entidad.merge(usuarios);
        entidad.getTransaction().commit();
        
        }catch(Exception e){
            
            entidad.getTransaction().rollback();
        }
        
    }
    
    public void eliminar(Usuarios usuarios){
        
        EntityManager entidad = entityManager();
        try{
        entidad.getTransaction().begin();
        entidad.remove(entidad.merge(usuarios));
        entidad.getTransaction().commit();
        
        }catch(Exception e){
            
            entidad.getTransaction().rollback();
        }
        
    }
    
}
