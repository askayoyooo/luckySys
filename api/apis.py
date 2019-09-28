import cv2
import numpy as np
import imutils


def template_matching(image_full_path, tmpl_full_path, min_confidence=0.93, ):
	img = cv2.imread(image_full_path)
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# template = cv2.imread(tmpl_full_path, cv2.IMREAD_GRAYSCALE)
	template = cv2.imread(tmpl_full_path)
	template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
	w, h = template.shape[::-1]
	res = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
	loc = np.where(res >= min_confidence)
	result_dic = {}
	confidence_list = []
	for pt in zip(*loc[::-1]):
		result_dic[res[pt[1]][pt[0]]] =pt
		confidence_list.append(res[pt[1]][pt[0]])
		cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 3)
	return result_dic, sorted(confidence_list, reverse=True)


def diff_size_template_matching(image_full_path, tmpl_full_path, min_confidence=0.95, ):
	template = cv2.imread(tmpl_full_path)
	template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

	image = cv2.imread(image_full_path)
	gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	result_dic = {}
	confidence_list = []
	for scale in np.linspace(0.2, 1.0, 100)[::-1]:
		print(scale)
		resized = imutils.resize(template, width=int(template.shape[1] * scale))
		(w, h) = resized.shape[::-1]
		result = cv2.matchTemplate(gray_img, resized, cv2.TM_CCOEFF_NORMED)
		loc = np.where(result >= min_confidence)
		print(loc)
		for pt in zip(*loc[::-1]):
			result_dic[result[pt[1]][pt[0]]] = pt
			confidence_list.append(result[pt[1]][pt[0]])
			cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 3)
	cv2.imshow("Visualize", image)
	cv2.waitKey(0)
	print(sorted(confidence_list, reverse=True))
	return result_dic, sorted(confidence_list, reverse=True)
