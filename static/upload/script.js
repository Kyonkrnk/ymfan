document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('chartForm');
    const difficultySlider = document.getElementById('difficultySlider');
    const difficultyValue = document.getElementById('difficultyValue');
    const bgmFileInput = document.getElementById('bgm_file');
    const jacketFileInput = document.getElementById('jacket_file');
    const chartFileInput = document.getElementById('chart_file');
    
    difficultyValue.textContent = difficultySlider.value;
    
    difficultySlider.addEventListener('input', function() {
        const value = difficultySlider.value;
        difficultyValue.textContent = value;
    });
    
    bgmFileInput.addEventListener('change', function() {
        const fileName = bgmFileInput.files[0].name;
        const label = bgmFileInput.nextElementSibling;
        label.textContent = fileName;
    });

    jacketFileInput.addEventListener('change', function() {
        const fileName = jacketFileInput.files[0].name;
        const label = jacketFileInput.nextElementSibling;
        label.textContent = fileName;
    });

    chartFileInput.addEventListener('change', function() {
        const fileName = chartFileInput.files[0].name;
        const label = chartFileInput.nextElementSibling;
        label.textContent = fileName;
    });
    
    form.addEventListener('submit', async function(event) {
        event.preventDefault();
        
        const formData = new FormData(form);
        
        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });
            
            if (response.ok) {
                alert('投稿完了！');
                form.reset();
            } else {
                alert('投稿に失敗しました。');
            }
        } catch (error) {
            alert('An error occurred while submitting the form.');
        }
    });
});