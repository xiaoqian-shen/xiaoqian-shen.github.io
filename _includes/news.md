<h2 id="news">News</h2>

<style>
  #scrollableDiv {
    min-height: 100px;
    height: 100px;
    overflow-y: hidden;
    opacity: 1;
    transition: height 0.5s ease-in-out, opacity 0.5s ease-in-out;
  }
</style>

<ul id="scrollableDiv" onmouseover="showScrollbar()" onmouseout="hideScrollbar()">
  <li><strong>[May. 2025]</strong> One paper (<a href="https://arxiv.org/abs/2410.17434">LongVU</a>) get accepted to ICML’25 🎉</li>
  <li><strong>[Feb. 2025]</strong> One paper (<a href="https://arxiv.org/abs/2312.02252">StoryGPT-V</a>) get accepted to CVPR’25 🎉</li>
  <li><strong>[July. 2024]</strong> Two papers (<a href="https://arxiv.org/abs/2407.12679">GoldFish</a>, <a href="https://arxiv.org/abs/2308.16349">AffectVisDial</a>) get accepted to ECCV’24</li>
  <li><strong>[Mar. 2024]</strong> One paper (<a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Haydarov_Adversarial_Text_to_Continuous_Image_Generation_CVPR_2024_paper.pdf">HyperCGAN</a>) gets accepted to CVPR’24</li>
  <li><strong>[Jan. 2024]</strong> One paper (<a href="https://arxiv.org/abs/2304.10592">MiniGPT-4</a>) gets accepted to ICLR’24</li>
  <li><strong>[Nov. 2023]</strong> Successfully defended my Master thesis</li>
  <li><strong>[July. 2023]</strong> One paper (<a href="https://arxiv.org/abs/2304.05390">HRS-Bench</a>) gets accepted to ICCV’23</li>
  <li><strong>[Feb. 2023]</strong> One paper (<a href="https://arxiv.org/abs/2304.02777">MoStGAN-V</a>) gets accepted to CVPR’23</li>
  <li><strong>[Sep. 2022]</strong> Started my Master journey at KAUST</li>
  <li><strong>[July. 2022]</strong> One paper (<a href="https://arxiv.org/abs/2203.01386">HGR-Net</a>) gets accepted to ECCV’22</li>
  <li><strong>[Dec. 2021]</strong> Joined Vision-CAIR at KAUST as a visiting research student</li>
</ul>

<p></p>
<script>
  function showScrollbar() {
    var div = document.getElementById('scrollableDiv');
    div.style.height = div.scrollHeight + 'px';
    div.style.opacity = 1;
  }
  function hideScrollbar() {
    var div = document.getElementById('scrollableDiv');
    div.style.height = '100px';
    div.style.opacity = 1;
  }
</script>