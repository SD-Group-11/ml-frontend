<template>
    <div class="container is-fluid"> 

    <div class="container is-fluid p-2">
        <div class="notification is-info has-text-centered" >
            <strong><h3 class="title is-1">Getting Started</h3></strong>
        </div>

    </div>


    <div class="container is-fluid p-2">
        <div class="notification is-info is-light has-text-centered" >
            <h3 class="title is-2">Uploading</h3>
        </div>

        <div>
           <ul class="steps is-vertical is-hollow is-dashed ">
              <li class="steps-segment is-active">
                <span class="steps-marker is-warning"></span>
                <div class="steps-content">
                  <!-- <code>is-primary</code> -->
                  <p class="is-size-4">Training dataset</p>
                  <p>Under your chosen model, use "Choose file" to select and upload your training dataset.</p>
                </div>
              </li>
              <li class="steps-segment">
                <span class="steps-marker is-warning"></span>
                <div class="steps-content">
                  <p class="is-size-4">Associated training dataset</p>
                  <p>Upload the test dataset that is associated with your uploaded training dataset.</p>
                  <!-- add picture -->
                </div>
              </li>
              <li class="steps-segment">
                <span class="steps-marker is-warning"></span>
                <div class="steps-content ">
                  <p class="is-size-4">Dataset Options</p>
                  <p>Download, view or delete datasets.</p>
                  <img src="@/assets/images/upload2NEW.png" alt="Logo" width="1200" height="1200">
                  <!-- add picture -->
                </div>
              </li>
              </ul>
        </div>
    </div>

    <div class="container is-fluid p-2">
        <div class="notification is-link is-light has-text-centered" >
            <h3 class="title is-2">Training</h3>
        </div>

        <div>
                  <ul class="steps is-vertical is-hollow is-dashed">
              <li class="steps-segment is-active">
                <span class="steps-marker is-warning"></span>
                <div class="steps-content">
                  <!-- <code>is-primary</code> -->
                  <p class="is-size-4">Select a dataset</p>
                  <p>Use the dropdown to select a dataset to train.</p>
                </div>
              </li>
              <li class="steps-segment">
                <span class="steps-marker is-warning"></span>
                <div class="steps-content">
                  <p class="is-size-4">Train</p>
                  <p>Click the "Train Model" button to display results.</p>
                </div>
              </li>
              <li class="steps-segment">
                <span class="steps-marker is-warning"></span>
                <div class="steps-content">
                  <p class="is-size-4">Results</p>
                  <p>Results will be displayed for you to interpret, download or discard.</p>
                  <img src="@/assets/images/training2.png" alt="Logo" width="1200" height="1200" >
                </div>
              </li>
              </ul>
        </div>
    </div>

    <div class="container is-fluid p-2">
        <div class="notification is-link is-light has-text-centered" >
            <h3 class="title is-2">Testing</h3>
        </div>

        <div>
            <ul class="steps is-vertical is-hollow is-dashed">
              <li class="steps-segment is-active">
                <span class="steps-marker is-warning"></span>
                <div class="steps-content">
                  <!-- <code>is-primary</code> -->
                  <p class="is-size-4">Select a trained model</p>
                  <p>Use the dropdown to select the trained model you want test. Testing can only be done on a trained model.</p>
                </div>
              </li>
              <li class="steps-segment">
                <span class="steps-marker is-warning"></span>
                <div class="steps-content">
                  <p class="is-size-4">Testing data</p>
                  <p>If there is no available test data, use the button on the testing page to upload one.</p>
                  <img src="@/assets/images/test.png" alt="Logo" width="10" height="10" class="center">
                </div>
              </li>
              <li class="steps-segment">
                <span class="steps-marker is-warning"></span>
                <div class="steps-content">
                  <p class="is-size-4">Test</p>
                  <p>Click the "Test Model" button to display results.</p>
                </div>
              </li>
              <li class="steps-segment">
                <span class="steps-marker is-warning"></span>
                <div class="steps-content">
                  <p class="is-size-4">Results</p>
                  <p>Results will be displayed for you to interpret, download or discard just like training results.</p>
                  <!-- <img src="@/assets/images/confused-icon-6-yellow.png" alt="Logo"> -->
                  <!-- can add images hooray :) -->
                </div>
              </li>
              </ul>
        </div>


  <!-- REUSING -->
    <!-- <div>
   <ul class="steps has-content-centered">
          <li class="steps-segment is-active is-dashed">
            <span class="steps-marker is-warning">1</span>
            <div class="steps-content"> --> 
              <!-- <p class="is-size-4">Step 1</p> -->
              <!-- <p class="is-size-5">Select an algorithm</p>
            </div>
          </li>

          <li class="steps-segment is-active is-dashed">
            <span class="steps-marker is-warning">2</span>
            <div class="steps-content">  -->
              <!-- <p class="is-size-4">Step 2</p> -->
              <!-- <p class="is-size-5">Upload a dataset</p>
            </div>
          </li>
        </ul>
  </div> -->

       

    </div>

    <!-- <div class="block" > </div> -->


    <!-- <div class="container p-5">
      <div class="control">
        <ul class="steps has-content-centered">
          <li class="steps-segment is-active is-dashed">
            <span class="steps-marker is-warning">1</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 1</p> -->
              <!-- <p class="is-size-5">Select an algorithm</p>
            </div>
          </li>
          <li class="steps-segment is-dashed">
            <span class="steps-marker">2</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 2</p> -->
              <!-- <p>Upload a dataset</p>
            </div>
          </li>
          <li class="steps-segment is-dashed">
            <span class="steps-marker ">3</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 3</p> -->
              <!-- <p>Train the model</p>
            </div>
          </li>
          <li class="steps-segment is-dashed">
            <span class="steps-marker">4</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 4</p> -->
              <!-- <p>Interpret the results</p>
            </div>
          </li>
          <li class="steps-segment is-dashed">
            <span class="steps-marker">5</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 5</p> -->
              <!-- <p> Download your results</p>
            </div>
          </li>
        </ul>
      </div> -->

      <!-- <div class="block" > </div>

      <div class="control">
        <div class="notification is-info is-light">
          Select model that best fits your data.
        </div>
      </div>
    </div>

    <div class="block" > </div> -->


    <!-- <div class="container p-5">
      <div class="control">
        <ul class="steps has-content-centered">
          <li class="steps-segment">
            <span class="steps-marker is-warning">1</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 1</p> -->
              <!-- <p class="is-size-5">Select an algorithm</p>
            </div>
          </li>
          <li class="steps-segment is-active is-dashed">
            <span class="steps-marker is-warning">2</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 2</p> -->
              <!-- <p class="is-size-5">Upload a dataset</p>
            </div>
          </li>
          <li class="steps-segment is-dashed">
            <span class="steps-marker ">3</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 3</p> -->
              <!-- <p>Apply the model</p>
            </div>
          </li>
          <li class="steps-segment is-dashed">
            <span class="steps-marker">4</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 4</p> -->
              <!-- <p>Interpret the results</p>
            </div>
          </li>
          <li class="steps-segment is-dashed">
            <span class="steps-marker">5</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 5</p> -->
              <!-- <p>Download your results</p>
            </div>
          </li>
        </ul>
      </div>

      <div class="block" > </div> -->

      <!-- <div class="control">
        <div class="notification is-info is-light">
          Upload dataset so it can be previewed, downloaded and stored for future use.
        </div>
      </div>
    </div> -->


    <!-- <div class="block" > </div>


    <div class="container p-5">
      <div class="control">
        <ul class="steps has-content-centered">
          <li class="steps-segment">
            <span class="steps-marker is-warning">1</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 1</p> -->
              <!-- <p class="is-size-5">Select an algorithm</p>
            </div>
          </li>
          <li class="steps-segment">
            <span class="steps-marker is-warning">2</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 2</p> -->
              <!-- <p class="is-size-5">Upload a dataset</p>
            </div>
          </li>
          <li class="steps-segment is-active is-dashed">
            <span class="steps-marker is-warning">3</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 3</p> -->
              <!-- <p class="is-size-5">Apply the model</p>
            </div>
          </li>
          <li class="steps-segment is-dashed">
            <span class="steps-marker">4</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 4</p> -->
              <!-- <p>Interpret the results</p>
            </div>
          </li>
          <li class="steps-segment is-dashed">
            <span class="steps-marker">5</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 5</p> -->
              <!-- <p>Download your results</p>
            </div>
          </li>
        </ul>
      </div> -->

      <!-- <div class="block" > </div>

      <div class="control">
        <div class="notification is-info is-light">
          Fill in hyper-parameters and click Train Model.
        </div>
      </div>
    </div> -->


    <!-- <div class="block" > </div>


    <div class="container p-5">
      <div class="control">
        <ul class="steps has-content-centered">
          <li class="steps-segment">
            <span class="steps-marker is-warning">1</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 1</p> -->
              <!-- <p class="is-size-5">Select an algorithm</p>
            </div>
          </li>
          <li class="steps-segment">
            <span class="steps-marker is-warning">2</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 2</p> -->
              <!-- <p class="is-size-5">Upload a dataset</p>
            </div>
          </li>
          <li class="steps-segment">
            <span class="steps-marker is-warning">3</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 3</p> -->
              <!-- <p class="is-size-5">Apply the model</p>
            </div>
          </li>
          <li class="steps-segment is-dashed is-active">
            <span class="steps-marker is-warning">4</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 4</p> -->
              <!-- <p class="is-size-5">Interpret the results</p>
            </div>
          </li>
          <li class="steps-segment is-dashed">
            <span class="steps-marker">5</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 5</p> -->
              <!-- <p>Download your results</p>
            </div>
          </li>
        </ul>
      </div>

      <div class="block" > </div>

      <div class="control">
        <div class="notification is-info is-light">
          Results will be graphically displayed.
        </div>
      </div>
    </div> -->

    <!-- <div class="block" > </div>


    <div class="container p-5">
      <div class="control">
        <ul class="steps has-content-centered">
          <li class="steps-segment">
            <span class="steps-marker is-warning">1</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 1</p> -->
              <!-- <p class="is-size-5">Select an algorithm</p>
            </div>
          </li>
          <li class="steps-segment">
            <span class="steps-marker is-warning">2</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 2</p> -->
              <!-- <p class="is-size-5">Upload a dataset</p>
            </div>
          </li>
          <li class="steps-segment">
            <span class="steps-marker is-warning">3</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 3</p> -->
              <!-- <p class="is-size-5">Apply the model</p>
            </div>
          </li>
          <li class="steps-segment">
            <span class="steps-marker is-warning">4</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 4</p> -->
              <!-- <p class="is-size-5">Interpret the results</p>
            </div>
          </li>
          <li class="steps-segment">
            <span class="steps-marker is-warning">5</span>
            <div class="steps-content"> -->
              <!-- <p class="is-size-4">Step 5</p> -->
              <!-- <p class="is-size-5">Download your results</p>
            </div>
          </li>
        </ul>
      </div>

      <div class="block" > </div>

      <div class="control">
        <div class="notification is-info is-light">
          View and optionally download the graphical results(.PNG, .SVG)
        </div>
      </div>
    </div> -->

  </div>  
</template>

<!-- <div class="github-card" data-github="SD-Group-11/ml-frontend" data-width="400" data-height="" data-theme="default"></div> -->


<style scoped>
  @import '../assets/styles/homepage.css';

  .card {
    /* max-width: 500px; */
    margin-left: auto;
    margin-right: auto;
  }

  img 
  { 
    padding: 15px;
    /* max-width:200%;
    height:200%; */
    /* resizing robot for landing page */
  }

  .center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 40%;
}

  
</style>


<script>
// @ is an alias to /src

export default {
  name: 'GettingStarted'
}
</script>
