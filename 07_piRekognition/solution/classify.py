import camera,polly,rekognition

def copyLocalFileToS3(filename, bucketName)
    boto3.client('s3').upload_file(filename, bucketName, filename)

if __name__ == "__main__":

	filename = "myimage.jpg"
	bucketname = YOUR_OWN_BUCKET

	takePicture(filename)

	copyLocalFileToS3(filename, bucketname)

	p = polly.connectToPolly()

	reko = rekognition.connectToRekognition()
	labels = rekognition.detectLabels(reko, filename)
	print labels

	top_label = labels[0]
	message = "I'm "+top_label['Confidence']+"% sure that this is a "+top_label['Name']+". "
	polly.speak(p, message)

        faces = rekognition.detectFaces(reko, image)
	print faces

	face_count = (str)(len(faces))
	message = face_count+" faces have been detected"
	polly.speak(p, message)

