<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>DCP Browser Worker - public </title>

  <!–– Load the dcp-client library ––>
    <script src="https://scheduler.distributed.computer/dcp-client/dcp-client.js"></script>

    <!–– Instantiate and run the DCP Browser Worker ––>
      <script>
        //Instantiate a DCP Browser Worker with paymentAddress (where Compute Credits are deposited) and maxWorkingSandboxes (number of concurrent sandboxes)
        const worker = new dcp.worker.Worker({
          paymentAddress: "OTcyNDk0NjYwNTk1NTAzMTM0.YnZ4Ow.EXqFhOqzdIMo7mxEcHPlIwN3dvQ",
          maxWorkingSandboxes: 4,
        });

        //Starts the DCP Browser Worker
        worker.start();

        //Optional events displayed in the console
        worker.on('fetchStart', () => {
          document.getElementById("events").appendChild(document.createElement('br'));
          document.getElementById("events").appendChild(document.createTextNode(`! fetching job slices...`));
        });

        worker.on('fetch', (fetchedSlicesCount) => {
          document.getElementById("events").appendChild(document.createElement('br'));
          document.getElementById("events").appendChild(document.createTextNode(`!   fetched ${fetchedSlicesCount} job slices, computing...`));
        });

        worker.on('submit', () => {
          document.getElementById("events").appendChild(document.createElement('br'));
          document.getElementById("events").appendChild(document.createTextNode(`! submitting computed job slice result...`));
        });

        worker.on('payment', receipt => {
          document.getElementById("events").appendChild(document.createElement('br'));
          document.getElementById("events").appendChild(document.createTextNode(`!   earned ${receipt.payment} Compute Credits`));
        });

      </script>

</head>

<body>
  Minimal DCP Browser Worker on the public network<br><br>
  To deploy a job, check out our DCP-Compute-API-toUpperCase replit<br>
  For more info, check out our <a href="https://docs.dcp.dev">Compute API</a><br>
  Reach out anytime at info@dcp.dev<br><br>
  Happy computing!<br><br>
  - DCP Team<br>
  <p>Worker log:<span id="events"></span></p>
</body>

</html>