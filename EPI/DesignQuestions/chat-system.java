import java.applet.Applet;
import java.awt.BorderLayout;
import java.awt.Panel;
import java.awt.TextArea;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Enumeration;
import java.util.Hashtable;


class Server
{
    private ServerScocket ss;
    private Hashtable OutputStreams =new Hashtable<>();
    public Server(int port) throws IOException
    {
        listen(port);
    }
    private void listen(int port)
    {
        ss=new ServerSocket(port);
        System.out.println("Listening on" + ss);
        while(true)
        {
            Socket s=ss.accept();
            System.out.println("Connection from " + s);
            DataOutputStream dout= new DataOutputStream(s.getOutputStream());
            OutputStreams.put(s, dout);
            
            new ServerThread(this,s);
        }
    }
    
    Enumeration getOutputStreams()
    {
        return OutputStreams.elements();
    }
    
    void sendToAll(String message)
    {
        synchronized (OutputStreams)
        {
            for(Enumeration e=getOutputStreams();e.hasMoreElements();)
            {
                DataOutputStream DOUT =(DataOutputStream)e.nextElement();
                try {
                    DOUT.writeUTF(message); 
                } catch(IOException ie) {
                    System.out.println(ie);
                }
            }
        }
    }
    
    void removeConnection(Socket s)
    {
        synchronized (OutputStreams)
        {
            System.out.println("Removing connection " + s);
            OutputStreams.remove(s);
            try {
                s.close();
            } catch(Exception e) {
                System.out.println("Error closing " +s);
            }
        }
    }
}

class ServerThread extends Thread
{
    private Server server;
    private Socket socket;
    
    public ServerThread(Server server,Socket socket)
    {
        this.server=server;
        this.socket=socket;
        start();
    }
    
    public void run()
    {
        try {
            DataInputStream din=new DataInputStream(socket.getInputStream());
            String message=din.readUTF();
            System.out.println("Sending " +message);
            server.sendToAll(message);
        } catch(EOFException e) {
            
        } catch (IOException e) {
            
        } finally {
            server.removeConnection(socket);
        }
    }
}

class Client extends Panel implements Runnable
{
    private TextField tf=new TextField();
    private TextArea ta=new TextArea();
    private Socket socket;
    private DataOutputStream dout;
    private DataInputStream din;
    
    public Client(final String host,final int port)
    {
        setLayout(new BorderLayout());
        add("North",tf);
        add("Center",ta);
        tf.addActionListener(new ActionListener()
        {
            @Override
            public void actionPerformed(ActionEvent arg0)
            {
                try {
                    socket =new Socket(host,port);
                    System.out.println("connected to " +socket);
                    din=new DataInputStream(socket.getInputStream());
                    dout=new DataOutputStream(socket.getOutputStream());
                    new Thread().start();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                
            }
        });
    }
    
    @Override
    public void run()
    {
        
        while(true)
        {
            try {
                String message=din.readUTF();
                ta.append(message + "\n");
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }
    }
    
    private void processMessage(String message)
    {
        try {
            dout.writeUTF(message);
            tf.setText(" ");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    
}

class ClientApplet extends Applet
{
    public void init()
    {
        String host=getParameter("host");
        int port=Integer.parseInt(getParameter("port"));
        setLayout(new BorderLayout());
        add("Center",new Client(host, port));
    }
}


public class SimpleChatServerTest {
    
    /**
    *
    */
    public SimpleChatServerTest() {
        // TODO Auto-generated constructor stub
    }
    
    /**
    * @param args
    */
    public static void main(String[] args)
    {
        int port=Integer.parseInt(args[0]);
        try {
            new Server(port);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }   
}
