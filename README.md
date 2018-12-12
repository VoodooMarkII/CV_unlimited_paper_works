# CV_unlimited_paper_works
## Feature
A simple script for downloading papers from CVPR and ICCV.

Download papers and supplymental material in PDF format.

I tested it by downloading CVPR 2018 papers. It should workwork on other CVF conference.

祝各位科研开坑愉快。
## How to Use
### Environment
**Python:**  (2.7.3+ or 3.2.2+ is better for using 'html.parser' to parse.)

**Beautiful Soup 4:** Install bs4

```bash
$ pip install beautifulsoup4
```

### Run

```bash
python main.py url
```
* `url`  The url of the conference papers page of the CVF. (Open Access version)
Default setting is downloading CVPR 2018.

#### Example

```bash
python main.py http://openaccess.thecvf.com/CVPR2018.py
```
This Example download the CVPR 2018 papers to the folder of this script.

## Notice
Due to some reason, download from Mainland China might be slow, please be patient, or use proxy to avoid this.
