import streamlit as st
from streamlit_image_comparison import image_comparison
import cv2


st.set_page_config("Photo retouching check in", "🔭", layout="centered")

st.header("🔭 Targeted dehighlighting around window")
st.markdown("### good case")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/2-wb.png",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/2-dehighlight_out.jpg",
    label1="MR, minus dehighlight",
    label2="with targeted dehighlight",
)

st.markdown("### worst case (different lighting variations in single photo)")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/6-wb.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/6-dehighlight_out.jpg",
    label1="MR, minus dehighlight",
    label2="with targeted dehighlight",
)

st.header("🔭 Automated white balance - default prompt: wall")
st.markdown("### good case")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/2_after_old.png",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/2-wb.png",
    label1="MR, minus white balance and targeted dehighlight",
    label2="added white balance",
)

st.markdown("### unsure case (is this too blue-ish?)")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/9_after_old.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/6-wb.png",
    label1="MR, minus white balance and targeted dehighlight",
    label2="added white balance",
)




st.header("🔭 Magic retouch")

st.write("")
"A combination of automated color correction tasks (mainly shadows lifting, dehighlighting, saturation and brightness adjustments)"
st.write("")

st.markdown("### test image 1")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/1.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/1_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 2")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/2.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/2_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 3")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/3.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/3_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 4")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/4.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/4_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 5")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/5.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/5_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 6")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/6.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/6_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 7")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/7.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/7_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 8")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/8.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/8_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 9")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/9.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/9_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 10")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/10.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/10_after.jpg",
    label1="input",
    label2="magic retouch",
)


st.header("🔭 magic retouching breakdown")

st.write("")
"when not combined as Magic Retouch, here are the individual result separated by algo group"
st.write("")


st.markdown("### shadows lifting")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/6.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/6_shadows.jpg",
    label1="input",
    label2="shadows lifting",
)

st.markdown("### dehighlighting")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/6.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/6_dehighlight.jpg",
    label1="input",
    label2="dehighlighting",
)

st.markdown("### brightness and brilliance")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/6.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/6_brilliance.jpg",
    label1="input",
    label2="brightened",
)

st.markdown("### targeted desaturation on red, yellow, orange colors (from client retouching note)")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/6.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/6_desaturation.JPG",
    label1="input",
    label2="targeted desaturation",
)

st.markdown("### white balance")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/6.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/6_wb.png",
    label1="input",
    label2="white balance",
)


st.header("🔭 Super resolution")

st.write("")
"also called upscaling, this will try to enhance details and generally make photo look a bit sharper. limited to 5MB max"
st.write("")


st.markdown("### upscaling - full")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/11_after.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/11_upscaled.jpg",
    label1="input",
    label2="upscaled",
    width=1000,
)

st.markdown("### upscaling - crop 1")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/11_after_1.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/11_upscaled_1.jpg",
    label1="input",
    label2="upscaled",
    width=1000,
)

st.markdown("### upscaling - crop 2")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/11_after_3.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/slider-demo/11_upscaled_3.jpg",
    label1="input",
    label2="upscaled",
    width=1000,
)
