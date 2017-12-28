# Picture to GDS
Python script to convert image files to GDSII files

## Getting Started
This is a simple script for generating GDSII layout files from image files. The input image files should have the extensions jpeg, jpg, png, pbm, pgm, or bmp. By specifying an image file, size of the unit-cell (minimum width and space of the layout), and layer number of the GDSII file, you can get a binary image file (image.bmp) and a GDSII layout file (image.gds).

### Prerequisites
```
NumPy
openCV
gdsCAD
```

## Usage
```
python picToGDS.py <fileName> <sizeOfTheCell[um]> <layerNum>
```

## Example
```
python picToGDS.py test.jpg 0.6 4
```
![example](https://github.com/ourfool/image-files/blob/master/picToGDS.jpg?raw=true
 "example")
 
## Author
* **Ourfool in Saginomiya** -[homepage](http://www.saginomiya.xyz/)-

## License
This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details
