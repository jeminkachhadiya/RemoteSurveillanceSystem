import argparse
import cv2
import os
import pafy


def frame_converter():
    source_type, source, target_dir, frame_no = opt.source_type, opt.source, opt.target_dir, opt.frame

    if source_type == 0:
        url = source
        video = pafy.new(url)
        best = video.getbest(preftype="mp4")
        capture = cv2.VideoCapture(best.url)
    else:
        capture = cv2.VideoCapture(source)
    try:
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
    except OSError:
        print('Error: Creating directory of data')

    currentframe = 0

    while True:
        ret, frame = capture.read()
        if ret:
            name = f'./{target_dir}/frame{str(currentframe)}.jpg'
            print('Creating...' + name)
            cv2.imwrite(name, frame)
            currentframe += frame_no
            capture.set(cv2.CAP_PROP_POS_FRAMES, currentframe)
        else:
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-type', type=int, default=0, help='0 for url and 1 for mp4 video')
    parser.add_argument('--source', type=str, default='', help='source in url or video file path')
    parser.add_argument('--target-dir', type=str, default='data', help='custom directory name to store images')
    parser.add_argument('--frame', type=int, default=60, help='number of frames need to skip')
    opt = parser.parse_args()
    print(opt)
    frame_converter()
