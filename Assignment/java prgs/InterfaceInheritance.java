
interface sample{
  void method1();
  void method2();
}

interface childSample extends sample{
  void method3();
  void method4();
}

class MySample implements childSample{
  public void method3(){
    System.out.println("method3");
  }
  
  public void method4(){
    System.out.println("method4");
  }
  
  public void method1(){
    System.out.println("method1");
  }
  
  public void method2(){
    System.out.println("method2");
  }
  
}


public class InterfaceInheritance {
    public static void main(String[] args) {
      
      MySample m = new MySample();
      
      m.method1();
      m.method2();
      m.method3();
      m.method4();
  }
}

