# uth-ear-book-dataset

This project provided annotation for ear disease from otoscopic images in the book https://med.uth.edu/orl/online-ear-disease-photo-book/.


The CSV annotation file format is described bellow:

| image_url | image_width | image_height | view_annotation_result_Polygon |
|-----------|------------|-------------|--------------------------------|
| https://med.uth.edu/orl/wp-content/uploads/sites/68/2017/10/Ch6_pic5LBL.jpg | 500 | 405 | `[{'points': [...], 'class_name': 'Eardrum'} ...` |


You can use the main.py function to visualize the annotation result by using the command:

```bash
python main.py annotation_file_name idx_to_visualize
```
E.g. You want to visualize the annotation of first image:
```bash
python main.py label_validation.csv 0
```
You will get results as bellow:
![Alt text](assests/eg1.png?raw=true "Visualization result")
