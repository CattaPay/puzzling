public class Piece {
    long[] bitmaps; 
    int[][] coords;
    char rep;
    int[] heights, widths;
    int height, width;
    int nCoords;
    int nOrientations;

    public Piece(int[][] coords, char rep){
        this.coords = coords;
        this.rep = rep;
        this.nCoords = coords.length;
        this.bitmaps = new long[8];
        this.heights = new int[8];
        this.widths = new int[8];
        this.getOrientations();
    }

    public long createBitmap() {
        long bits = 0;
        for (int i = 0; i < 8; i++){
            for (int j = 0; j < 8; j++){
                bits <<= 1;
                for (int k = 0; k < nCoords; k++) {
                    if (coords[k][0] == i & coords[k][1] == j){
                        bits++;
                    }
                }
            }
        }
        return bits;
    }

    public void updateDims(){
        height = 0;
        width = 0;
        for (int i = 0; i < nCoords; i++) {
            if (height < coords[i][0]){
                height = coords[i][0];
            }
            if (width < coords[i][1]) {
                width = coords[i][1];
            }
        }
        height++;
        width++;
    }

    public int[][] rotate(){
        int[][] newCoords = new int[this.nCoords][2];
        int min_x = Integer.MAX_VALUE;
        int min_y = Integer.MAX_VALUE;

        for (int i = 0; i < this.nCoords; i++){
            newCoords[i][0] = -this.coords[i][1];
            if (min_x > newCoords[i][0]){
                min_x = newCoords[i][0];
            }

            newCoords[i][1] = this.coords[i][0];
            if (min_y > newCoords[i][1]){
                min_y = newCoords[i][1];
            }
        }

        for (int i = 0; i < this.nCoords; i++) {
            newCoords[i][0] -= min_x;
            newCoords[i][1] -= min_y;
        }

        return newCoords;
    }

    public int[][] flip(){
        int[][] newCoords = new int[this.nCoords][2];
        int min_x = Integer.MAX_VALUE;

        for (int i = 0; i < nCoords; i++) {
            newCoords[i][0] = -coords[i][0];
            newCoords[i][1] = coords[i][1];
            if (newCoords[i][0] < min_x){
                min_x = newCoords[i][0];
            }
        }

        for (int i = 0; i < nCoords; i++) {
            newCoords[i][0] -= min_x;
        }
        return newCoords;
    }

    public void rotateThis(){
        this.coords = this.rotate();
    }

    public void flipThis(){
        this.coords = this.flip();
    }

    public void getOrientations(){
        long bitmap;
        Boolean flag;
        this.updateDims();
        nOrientations = 0;
        // first orientation
        bitmaps[nOrientations] = this.createBitmap();
        heights[nOrientations] = height;
        widths[nOrientations] = width;
        nOrientations++;
        
        for (int i = 0; i < 3; i++){
            this.rotateThis();
            bitmap = this.createBitmap();
            flag = Boolean.FALSE;
            for (long l : bitmaps) {
                if (l == bitmap) {
                    flag = Boolean.TRUE;
                }
            }
            if (!flag){
                this.updateDims();
                bitmaps[nOrientations] = this.createBitmap();
                heights[nOrientations] = height;
                widths[nOrientations] = width;
                nOrientations++;
            }
        }

        this.flipThis();
        for (int i = 0; i < 4; i++){
            this.rotateThis();
            bitmap = this.createBitmap();
            flag = Boolean.FALSE;
            for (long l : bitmaps) {
                if (l == bitmap) {
                    flag = Boolean.TRUE;
                }
            }
            if (!flag){
                this.updateDims();
                bitmaps[nOrientations] = this.createBitmap();
                heights[nOrientations] = height;
                widths[nOrientations] = width;
                nOrientations++;
            }
        }      
        
    }

    public void print(){
        for (int i = 0; i < nCoords; i++) {
            System.out.println(String.format("%d, %d", coords[i][0], coords[i][1]));
        }
    }

    public void printGrid(){
        String strout = "";
        boolean contains;
        for (int i = 0; i < 8; i++){
            for (int j = 0; j < 8; j++){
                contains = Boolean.FALSE;
                for (int k = 0; k < nCoords; k++) {
                    if (coords[k][0] == i & coords[k][1] == j){
                        contains = Boolean.TRUE;
                    }
                }
                if (contains){
                    strout += "X ";
                }
                else{
                    strout += "O ";
                }
            }
            strout += "\n";
        }
        System.out.println(strout);
    }
    
    public void printOrientations(){
        for (int k = 0; k < nOrientations; k++) {
            long bits = bitmaps[k];
            long bit;
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8; j++) {
                    bit = (bits >> (63 - (i * 8 + j))) & 1;
                    System.out.print(bit == 1 ? this.rep + " " : "O ");
                }
                System.out.println();
            }
            System.out.println();

        }
    }
}
