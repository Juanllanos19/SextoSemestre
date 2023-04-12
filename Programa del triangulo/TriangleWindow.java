import javax.swing.*;
import java.awt.*;

public class TriangleWindow extends JFrame{

//Declaración de los componentes de interfaz
  JLabel lado1Lbl, lado2lbl, lado3lbl;
  JTextField lado1txtFld, lado2txtFld, lado3txtFld;
  JButton calcularBtn;
  JTextArea areaResultadoTxtArea;


  //Construimos la clase de tipo ventana 

  public TriangleWindow(){

    //cambiamos el título de la ventana en el constructor
    super ("Tipo de triangulo");

    //Construimos el contenido de la ventana en un contenedor para la ventana
    Container container = getContentPane();
    container.setLayout (new FlowLayout());

    lado1Lbl=new JLabel ("Lado 1");
    lado1txtFld=new JTextField(10);
    container.add(lado1Lbl);
    container.add(lado1txtFld);
    
    lado2lbl=new JLabel ("Lado 2");
    lado2txtFld=new JTextField(10); 
    container.add(lado2lbl);
    container.add(lado2txtFld);
    
    lado3lbl=new JLabel ("Lado 3");
    lado3txtFld =new JTextField(10);
    container.add(lado3lbl);
    container.add(lado3txtFld);

    calcularBtn= new JButton ("identificar triangulo");
    container.add(calcularBtn);
    calcularBtn.addActionListener (new Handler (this)); //Agregamos un escuchador de eventos al botón la clase Handler implementa la funcionalidad

    areaResultadoTxtArea = new JTextArea(12,12);
    container.add(areaResultadoTxtArea);
    
    //Mostramos la ventana
    setSize (180, 200);
    setVisible(true);
  }
}