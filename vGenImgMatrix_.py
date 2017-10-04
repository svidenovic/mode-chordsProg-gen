
import vMatrixSizeCalculator_, os;
from PIL import Image;

def create_img_matrix( tmp_imgs_folder, img_path ):
	print(" Creating Image Matrix... ",end="");
	imgs = [];
	for imgf in os.listdir( tmp_imgs_folder ):
		imgs.append( Image.open(tmp_imgs_folder+"/"+imgf) );

	[rows,cols] = vMatrixSizeCalculator_.gen_MatrixSize( len(imgs) );

	imgMatrix_size = [rows*imgs[0].width, cols*imgs[0].height];
	imgMatrix = Image.new("RGBA",(imgMatrix_size[0],imgMatrix_size[1]));

	img_i = 0;
	for row in range(0, imgMatrix_size[1], imgs[0].height):
		for col in range(0, imgMatrix_size[0], imgs[0].width):
			imgMatrix .paste( imgs[img_i], (col,row) );
			img_i += 1;
			if img_i == len(imgs):
				break;
		if img_i == len(imgs):
			break;

	imgMatrix.save(img_path);

	for img in imgs:
		img.close();
		
	print("Done");
