public class Triangle {

  public String identificarTriangulo(String lado1, String lado2, String lado3) {
      int a = Integer.parseInt(lado1); //Convierte una cadena de texto en un número entero
      int b = Integer.parseInt(lado2);
      int c = Integer.parseInt(lado3);

      if (a == 0 || b == 0 || c == 0) {
          return "El traingulo no puedo ser formado";
      } else {
          return "El triangulo es " + typeTriangle(a, b, c);
      }
  }

  public String typeTriangle(int a, int b, int c) {
      if (a == b && b == c)
          return "Equilatero";
      else if (a == b || b == c || a == c)
          return "Isosceles";
      else
          return "Escaleno";
  }
}
