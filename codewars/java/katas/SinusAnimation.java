import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SinusAnimation extends JFrame {
    
    private AnimationPanel animationPanel;
    private Timer timer;
    private int speed = 10; // initial speed

    public SinusAnimation() {
        setTitle("Sinus Animation");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        animationPanel = new AnimationPanel();
        add(animationPanel, BorderLayout.CENTER);

        JPanel controlPanel = new JPanel();
        JButton increaseSpeedButton = new JButton("+");
        JButton decreaseSpeedButton = new JButton("-");

        increaseSpeedButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (speed > 1) {
                    speed -= 1;
                    timer.setDelay(speed);
                }
            }
        });

        decreaseSpeedButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                speed += 1;
                timer.setDelay(speed);
            }
        });

        controlPanel.add(increaseSpeedButton);
        controlPanel.add(decreaseSpeedButton);
        add(controlPanel, BorderLayout.SOUTH);

        timer = new Timer(speed, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                animationPanel.updatePoints();
            }
        });
        timer.start();
    }

    private class AnimationPanel extends JPanel {
        private int[] xPoints = new int[10];
        private int[] yPoints = new int[10];
        private double angle = 0;

        public AnimationPanel() {
            for (int i = 0; i < xPoints.length; i++) {
                xPoints[i] = i * 80;
                yPoints[i] = getHeight() / 2;
            }
        }

        public void updatePoints() {
            angle += 0.1;
            for (int i = 0; i < xPoints.length; i++) {
                yPoints[i] = (int) (getHeight() / 2 + 100 * Math.sin(angle + i * 0.5));
            }
            repaint();
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            g.setColor(Color.RED);
            for (int i = 0; i < xPoints.length; i++) {
                g.fillOval(xPoints[i], yPoints[i], 10, 10);
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new SinusAnimation().setVisible(true);
            }
        });
    }
}
