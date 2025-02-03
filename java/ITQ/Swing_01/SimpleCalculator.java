import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SimpleCalculator {
    public static void main() {
        JFrame frame = new JFrame("Einfacher Taschenrechner");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 400);

        // Erstelle ein Panel mit GridLayout für die Tasten
        JPanel panel = new JPanel(new GridLayout(4, 4, 10, 10));

        // Erstelle ein Textfeld zur Anzeige der Eingabe und des Ergebnisses
        JTextField display = new JTextField();
        display.setEditable(false);
        display.setHorizontalAlignment(JTextField.RIGHT);

        // Erstelle die Tasten
        String[] buttons = {
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "=",
            "0", " ", " ", "x²"
        };

        // Füge die Tasten dem Panel hinzu
        for (String text : buttons) {
            JButton button = new JButton(text);
            panel.add(button);

            // Füge ActionListener zu den Tasten hinzu
            button.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    // Hier kann die Logik für den Taschenrechner implementiert werden
                    String command = e.getActionCommand();
                    // Beispielhafte Logik (ohne tatsächliche Berechnung)
                    if ("=".equals(command)) {
                        // Berechne das Ergebnis (hier nur als Platzhalter)
                        display.setText("Ergebnis");
                    } else {
                        // Füge die gedrückte Taste dem Display hinzu
                        display.setText(display.getText() + command);
                    }
                }
            });
        }

        // Füge das Display und das Panel dem Frame hinzu
        frame.setLayout(new BorderLayout());
        frame.add(display, BorderLayout.NORTH);
        frame.add(panel, BorderLayout.CENTER);

        // Zeige das Fenster
        frame.setVisible(true);
    }
}
