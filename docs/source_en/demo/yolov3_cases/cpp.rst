C++ Codes Explanation
_____________________

Case 0: decoding and preprocessing with opencv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    In this case, we detect objects in multiple videos with a bmodel converted by yolov3.
    We use public released opencv to decode videos and process images.
    In the function of do_inference, we first initialize instances of sail::Engine, PreProcessor, PostProcessor:
    
        .. code-block:: cpp

           // ...
           // sail Engine ele
           sail::Engine engine(bmodel_path, tpu_id, sail::SYSIO);
           
           // ...
           // preforward
           PreProcessor preprocessor(416, 416);
           
           // ...
           // postforward
           PostProcessor postprocessor(0.5);
           
           // ...


    Then, we use a while-loop to process each frame of the video.
    The core of the pipeline are decoding, preprocessing, inference, postprocessing.
    
        .. code-block:: cpp

           // ...
           // using opencv cap get video frame
           while (cap.read(frame)) {
           
             // ...
             // preforward
             preprocessor.processv2(input, frame);
             
             // ...
             // forward
             engine.process(graph_name);
             
             // ...
             // postforward include NMS
             auto result = postprocessor.process(output, output_shape[2], height, width);



Case 1: decoding with bm-ffmpeg and preprocessing with bmcv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    In case 1, we use bm-ffmpeg and bmcv for decoding and preprocessing instead of public released opencv.
    Thus, FFMpegFrameProvider which is defined in "frame_provider.h" and encapsulated sail::Decoder, sail::Bmcv is used to decoding input videos.
    And, PreProcessorBmcv is used to processing image tensor before inference.
    
        .. code-block:: cpp
    
           // ...
           PreProcessorBmcv preprocessor(bmcv, input_scale, 416, 416);
           PostProcessor postprocessor(0.5);

           // ...
           // bm-ffmpeg ele
           FFMpegFrameProvider frame_provider(bmcv, input_path, tpu_id);
           // bmcv ele
           sail::BMImage img0, img1;

           // ...
           // using bmcv-ele get frame
           while (!frame_provider.get(img0)) {

             // ...
             // preforward
             preprocessor.process(img0, img1);
             
             // ...
             // forward
             engine.process(graph_name);

             // ...
             // postforward include NMS
             auto result = postprocessor.process(output, output_shape[2], height, width);




