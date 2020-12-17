# Topic Detection

**Nhóm 11**

## Slide báo cáo

File: [project_report.pdf](./project_report.pdf)

Nội dung:

- Mô tả về phương pháp làm sạch dữ liệu, thu thập thông tin và visualize dữ liệu.
- Mô tả về hai thuật toán sử dụng: TFIDF và SVM.
- Kết quả thử nghiệm và giải thich.

## Train mô hình dự đoán

File: [topic_detection_train.ipynb](./topic_detection_train.ipynb)

Thực hiện quá trình phân tích dữ liệu, huấn luyện mô hình, đánh giá kết quả mô hình và xuất mô hình ra file [trained_model.sav](./trained_model.sav).

## Đưa ra dự đoán với bộ dữ liệu test

File: [topic_detection_test.ipynb](./topic_detection_test.ipynb)

Sử dụng file [data_prep](./data_prep.py) để thực hiện tiền xử lý dữ liệu và đưa ra dự đoán bằng file [trained_model.sav](./trained_model.sav).

## Tiền xử lý dữ liệu

File: [data_prep.py](./data_prep.py)

Thực hiện quá trình làm sạch dữ liệu, bao gồm:

- Loại bỏ đường dẫn, số điện thoại, email, thẻ html...
- Loại bỏ emoji
- Đưa văn bản về dạng chữ thường, chuẩn hóa dấu câu
- Loại bỏ khoảng trằng thừa
- Loại bỏ stopword có trong [danh sách](./vietnamese-stopwords-dash.txt)
