public class point {
    private int x;
    private int y;
    
    public point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void move(int dx, int dy) {
        this.x += dx;
        this.y += dy;
    }

    @Override
    public String toString() {
        return "point(" + this.x + "|" + this.y + ")";
    }    
}
