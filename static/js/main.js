// Traffic Sign Recognition System - JavaScript Functionality

$(document).ready(function () {
    console.log("Traffic Sign Recognition System loaded successfully!");
    
    // Test if elements exist
    console.log("Elements check:");
    console.log("- Image upload:", $("#imageUpload").length > 0);
    console.log("- Image section:", $("#image-section").length > 0);
    console.log("- Predict button:", $("#btn-predict").length > 0);
    
    // Handle file selection and image preview
    $("#imageUpload").change(function () {
        console.log("File input changed");
        
        // Hide previous results
        $("#image-section").hide();
        $("#result").hide();
        $("#loader").show();

        if (this.files && this.files[0]) {
            console.log("Valid file selected:", this.files[0].name);
            
            // Validate file type
            const validTypes = ['image/jpeg', 'image/jpg', 'image/png'];
            if (!validTypes.includes(this.files[0].type)) {
                alert('Please select a valid image file (JPG, JPEG, or PNG)');
                $("#loader").hide();
                return;
            }
            
            // Validate file size (max 5MB)
            if (this.files[0].size > 5 * 1024 * 1024) {
                alert('File size too large. Please select an image under 5MB.');
                $("#loader").hide();
                return;
            }
            
            var reader = new FileReader();
            reader.onload = function (e) {
                console.log("FileReader loaded image successfully");
                
                // Set the background image of the preview div
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview').hide();
                $('#imagePreview').fadeIn(650);
                
                // Show the predict button section
                $("#loader").hide();
                $("#image-section").show();
                console.log("Image preview and predict button now visible");
            }
            
            reader.onerror = function() {
                console.error("Error reading file");
                $("#loader").hide();
                alert('Error reading the selected file. Please try again.');
            }
            
            reader.readAsDataURL(this.files[0]);
        } else {
            console.log("No valid file selected");
            $("#image-section").hide();
            $("#loader").hide();
            $("#result").hide();
        }
    });

    // Handle prediction button click
    $('#btn-predict').click(function () {
        console.log("Predict button clicked");
        
        // Validate that a file is selected
        if (!$("#imageUpload")[0].files || !$("#imageUpload")[0].files[0]) {
            alert('Please select an image first!');
            return;
        }
        
        var form_data = new FormData($('#upload-file')[0]);
        
        // Show loading state
        $(this).prop('disabled', true);
        $(this).html('🔄 Processing...');
        $("#loader").show();
        $("#result").hide();

        // Send AJAX request to Flask backend
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            timeout: 30000, // 30 second timeout
            success: function (data) {
                console.log('Prediction successful:', data);
                
                // Hide loader and restore button
                $("#loader").hide();
                $('#btn-predict').prop('disabled', false);
                $('#btn-predict').html('🔍 Predict Traffic Sign!');
                
                // Show result with animation
                $("#result").removeClass('error').addClass('success');
                $("#result").html('🎯 ' + data);
                $("#result").fadeIn(600);
                
                // Add some celebration effect
                if (data.includes('Confidence:')) {
                    const confidence = parseFloat(data.match(/(\d+\.?\d*)%/)[1]);
                    if (confidence > 80) {
                        $("#result").append(' 🎉');
                    } else if (confidence > 60) {
                        $("#result").append(' 👍');
                    } else {
                        $("#result").append(' 🤔');
                    }
                }
            },
            error: function (xhr, status, error) {
                console.error('Prediction error:', error);
                console.error('Status:', status);
                console.error('Response:', xhr.responseText);
                
                // Hide loader and restore button
                $("#loader").hide();
                $('#btn-predict').prop('disabled', false);
                $('#btn-predict').html('🔍 Predict Traffic Sign!');
                
                // Show error message
                $("#result").removeClass('success').addClass('error');
                let errorMessage = '❌ Prediction failed. ';
                
                if (status === 'timeout') {
                    errorMessage += 'Request timed out. Please try again.';
                } else if (xhr.status === 500) {
                    errorMessage += 'Server error. Please check if the model file is loaded.';
                } else if (xhr.status === 0) {
                    errorMessage += 'Network error. Please check your connection.';
                } else {
                    errorMessage += 'Please try again or check the console for details.';
                }
                
                $("#result").html(errorMessage);
                $("#result").fadeIn(600);
            }
        });
    });
    
    // Add drag and drop functionality
    const uploadSection = $('.upload-section')[0];
    
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        uploadSection.addEventListener(eventName, preventDefaults, false);
    });
    
    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }
    
    ['dragenter', 'dragover'].forEach(eventName => {
        uploadSection.addEventListener(eventName, highlight, false);
    });
    
    ['dragleave', 'drop'].forEach(eventName => {
        uploadSection.addEventListener(eventName, unhighlight, false);
    });
    
    function highlight(e) {
        uploadSection.classList.add('drag-over');
    }
    
    function unhighlight(e) {
        uploadSection.classList.remove('drag-over');
    }
    
    uploadSection.addEventListener('drop', handleDrop, false);
    
    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        
        if (files.length > 0) {
            $("#imageUpload")[0].files = files;
            $("#imageUpload").trigger('change');
        }
    }
    
    // Add some CSS for drag and drop
    $('<style>')
        .prop('type', 'text/css')
        .html(`
            .drag-over {
                border: 3px dashed #3498db !important;
                background: rgba(52, 152, 219, 0.1) !important;
                transform: scale(1.02);
            }
        `)
        .appendTo('head');
    
    // Add keyboard shortcuts
    $(document).keydown(function(e) {
        // Press 'P' to trigger prediction
        if (e.key === 'p' || e.key === 'P') {
            if ($("#btn-predict").is(':visible') && !$("#btn-predict").prop('disabled')) {
                $("#btn-predict").click();
            }
        }
        
        // Press 'U' to trigger file upload
        if (e.key === 'u' || e.key === 'U') {
            $("#imageUpload").click();
        }
    });
    
    console.log("All event handlers initialized successfully!");
    console.log("Keyboard shortcuts: 'U' for upload, 'P' for predict");
});