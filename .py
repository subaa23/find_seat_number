import java.util.*;

public class Main {
    public static void main(String[] args) {
        System.out.print("ENTER SEAT NUMBER:");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        
        num = num % 8; // Reduce seat number to a value between 0 and 7
        
        if (num == 1 || num == 4) {
            System.out.print("LOWER");
        } else if (num == 2 || num == 5) {
            System.out.print("MIDDLE");
        } else if (num == 3 || num == 6) {
            System.out.print("UPPER");
        } else if (num == 7) {
            System.out.print("SIDE LOWER");
        } else if (num == 0) { // Seats numbered 8 will have a remainder of 0
            System.out.print("SIDE UPPER");
        } else {
            System.out.print("NO SUCH SEATS AVAILABLE");
        }
    }
}
