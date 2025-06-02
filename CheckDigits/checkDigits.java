
public class checkDigits {
    public static boolean onlyDigits(String s){
        for (int i=0; i<s.length(); i++){
            if (!Character.isDigit(s.charAt(i))){
                return false;
            }
        } 
        return true;
    }

    public static void main(String[] args) {
        System.out.println(onlyDigits("12345"));
        System.out.println(onlyDigits("abc123"));
    }
}