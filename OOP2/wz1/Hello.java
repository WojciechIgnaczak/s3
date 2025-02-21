public class Hello 
{
  public static void main(String[] args)
  {
    boolean b = 2>1;
    if (b)
    {
      System.out.println("TTT");
    }
    byte b1=64;// byte - 8bit -128 to 127
    System.out.println(b1);
    b1=-126;
    System.out.println(b1);
    char c='a';// 16 bit
    System.out.println(c);
    c='\u0104';
    System.out.println(c);

    // short s; //16bit
    // System.out.println(s);

    // int i;//32bit
    // System.out.println(i);

    // long l;//64bit
    // System.out.println(l);
    
    float f=1.2f; //32 bit
    Float ff= new Float(f);
    System.out.println(ff);
    System.out.println(Float.MAX_VALUE);
    System.out.println(ff.toString());
    System.out.println((int)Character.MAX_VALUE);
    double d=1.3; // 64 bit
    System.out.println(d);


    long l=123_456_789_0L;// _ rozdzielacze między cyframi pomijane przez kompilator
    System.out.println(l);

  }
}
