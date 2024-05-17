public class Board {
    // creates a board up to 8x8 with blockers blocked off
    long bitmap;
    int height, width;
    int[][] blockers;
    int[][] coords;
    public Board(int height, int width, int[][] blockers){
        this.height = height;
        this.width = width;
        bitmap = 0;
        this.blockers = blockers;

        bitmap = this.createBitmap();
    }

    public long createBitmap() {
        long bits = 0;
        Boolean flag;
        for (int i = 0; i < 8; i++){
            for (int j = 0; j < 8; j++){
                bits <<= 1;
                flag = Boolean.FALSE;
                for (int k = 0; k < blockers.length; k++) {
                    if (blockers[k][0] == i & blockers[k][1] == j){
                        flag = Boolean.TRUE;
                    }
                    if (i >= height || j >= width) {
                        flag = Boolean.TRUE;
                    }
                }
                if (!flag){
                    bits += 1;
                }
            }
        }
        return ~bits;
    }

    public void print(){
        long bit;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                bit = (bitmap >> (63 - (i * 8 + j))) & 1;
                System.out.print(bit == 1 ? "X " : "O ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
