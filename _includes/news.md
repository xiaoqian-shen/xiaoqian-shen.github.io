<h2 id="news">News</h2>

<style>
  #scrollableDiv {
    width: 900px;
    min-height: 100px;
    height: 100px;
    overflow-y: hidden;
    opacity: 1;
    transition: height 0.5s ease-in-out, opacity 0.5s ease-in-out;
  }
</style>

<div id="scrollableDiv" onmouseover="showScrollbar()" onmouseout="hideScrollbar()">
    <ul>
      <li><strong>[Nov. 2023]</strong> Successfully defended my Master thesis</li>
      <li><strong>[July. 2023]</strong> One paper (HRS-Bench) gets accepted to ICCV’23</li>
      <li><strong>[Apr. 2023]</strong> We released MiniGPT-4 and received GitHub 10k stars in 3 days</li>
      <li><strong>[Feb. 2023]</strong> One paper (MoStGAN-V) gets accepted to CVPR’23</li>
      <li><strong>[Sep. 2022]</strong> Started my Master journey at KAUST</li>
      <li><strong>[July. 2022]</strong> One paper gets accepted to ECCV’22</li>
      <li><strong>[Dec. 2021]</strong> Joined Vision-CAIR at KAUST as a visiting research student</li>
    </ul>
</div>
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