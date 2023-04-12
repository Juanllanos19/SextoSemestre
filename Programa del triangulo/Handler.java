import java.awt.*;  
import java.awt.event.*;

import javax.swing.JTextArea;  

public class Handler implements ActionListener{

  //Clase especializada en identificar el tipo de triangulo
  Triangle triangulo;
  //Ventana observada
  TriangleWindow window;

  //datos capturados en la ventana en los campos de texto
  String lado1, lado2, lado3;

  //Cadena de texto para comunicar el resultado
  String resultado="Por implementar"; 

  public Handler (TriangleWindow w){
    triangulo = new Triangle ();
    this.window = w;
  }

  //función que reacción al click del botón
  public void actionPerformed (ActionEvent e){

    //get dat from textFields
    lado1= window.lado1txtFld.getText();
    lado2= window.lado2txtFld.getText();
    lado3= window.lado3txtFld.getText();
    
    //Call methods to check the triangle 
    resultado = triangulo.identificarTriangulo (lado1,lado2,lado3);
    //mostrar en el textarea el mensaje de texto correspondiente
    window.areaResultadoTxtArea.setText(resultado);
  }
}