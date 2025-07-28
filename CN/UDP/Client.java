import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;

public class Client
{
    public static void main(String args[]) throws IOException
    {
        Scanner sc = new Scanner(System.in);

        // Step 1:Create the socket object for
        // carrying the data. Client runs on port 8080
        DatagramSocket ds = new DatagramSocket(8080);

        InetAddress ip = InetAddress.getLocalHost();
        byte buf[] = null;

        System.out.println("UDP Client started on port 8080");
        System.out.println("Connecting to server on port 9090");
        System.out.println("Enter messages (type 'bye' to exit):");

        // loop while user not enters "bye"
        while (true)
        {
            String inp = sc.nextLine();

            // convert the String input into the byte array.
            buf = inp.getBytes();

            // Step 2 : Create the datagramPacket for sending
            // the data to server port 9090.
            DatagramPacket DpSend =
                  new DatagramPacket(buf, buf.length, ip, 9090);

            // Step 3 : invoke the send call to actually send
            // the data.
            ds.send(DpSend);

            // break the loop if user enters "bye"
            if (inp.equals("bye"))
                break;
        }
    }
}